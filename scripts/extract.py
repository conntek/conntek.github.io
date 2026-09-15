"""把 cache/ 里的原始 HTML 抽成结构化数据 cache/site.json，供 build.py 按统一模板渲染。

只抽内容，不管排版：产品(简介/优势/规格表/示意图/文档/视频)、类目、应用、服务、技术洞见、关于、联系。
资源路径统一成 /images /videos /files 下的本地路径，远端地址记在 assets 里。
"""
import json, os, re, urllib.parse
from bs4 import BeautifulSoup, Comment

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://www.conntek.com.cn'
IDX = json.load(open(os.path.join(ROOT, 'cache', 'index.json'), encoding='utf-8'))
ASSETS = {}

CATS = [
    ('3d-hall', '3D霍尔芯片', 'magneticAngleDetectionChip'),
    ('encoder', '编码器芯片', 'magneticCurrentLinearSensingChip'),
    ('switch', '开关芯片', 'switchPositionDetectionChip'),
    ('other', '其他芯片', 'signalConditioningChip'),
    ('knob', '旋钮系列', 'kuntaixuanniuserise'),
]
PRODUCT_SLUG = {
    '57xilie': 'kth57', 'magneticAngleEncoderChip': 'kth57', 'kth5502': 'kth55',
    'KTM52XX': 'ktm52', 'KTM53XX': 'ktm53', 'absoluteangledivider': 'ktm58',
    'hshrTMPMagnrticEncoderChip': 'ktm59', 'hshrMagneticCodedAngleSensor': 'kth78',
    'magneticencoder': 'kth71', 'cursorabsoluteencoder': 'kto95',
    'microPowerSeries': 'kth16', 'automotiveHvdlHallEffectSensor': 'kth25',
    'magnetoresistiveSwitchSeries': 'ktm13', 'hvcpDetectionSensor': 'ktm28',
    'proportionallinerhalleffectsensor': 'kth31', 'highlysensitive3dhallswitch': 'kth460',
    'highsensitive2Dhallswitch': 'kth462', 'linearHallChip': 'linear-hall',
    'zeroDriftAmplifierChip': 'ktax33', 'kuntaixuanniu': 'knob',
}
LEGACY = {'linearHallChip': ('switch', '线性霍尔芯片')}
APPS = [
    ('consumer-electronics', '消费类电子', 'consumerElectronics', 'Consumer Electronics'),
    ('intelligent-life', '智能生活', 'intelligentLife', 'Intelligent Life'),
    ('industry4', '工业4.0', 'industry4', 'Industrial 4.0'),
    ('intelligent-transportation', '智能交通', 'intelligentTransportation', 'Intelligent Transportation'),
]


def soup(path):
    s = BeautifulSoup(open(os.path.join(ROOT, 'cache', IDX['pages'][path]), encoding='utf-8').read(), 'html.parser')
    for t in s(['script', 'style', 'noscript']):
        t.decompose()
    for t in s.find_all(string=lambda x: isinstance(x, Comment)):
        t.extract()
    return s


def text(node):
    return re.sub(r'\s+', ' ', node.get_text(' ', strip=True)).strip() if node else ''


def lines(node):
    if not node:
        return []
    for br in node.find_all('br'):
        br.replace_with('\n')
    for p in node.find_all(['p', 'li', 'div']):
        p.insert_after('\n')
    return [re.sub(r'\s+', ' ', l).strip() for l in node.get_text().split('\n') if l.strip()]


def asset(src, kind='images'):
    u = urllib.parse.urljoin(BASE + '/', src.strip())
    p = urllib.parse.urlparse(u)
    name = urllib.parse.unquote(p.path)
    if 'conntek.com.cn' not in p.netloc:
        name = '/ext/' + os.path.basename(name)
    name = re.sub(r'^/(template/1/conntekCompany/(Picture|Images|videos)|upload/1/cms/(content/editor|content|category))/', '', name)
    local = f'/{kind}/' + name.lstrip('/')
    ASSETS[local] = urllib.parse.urlunsplit(urllib.parse.urlsplit(u)._replace(path=urllib.parse.quote(urllib.parse.unquote(p.path))))
    return local


def product_route(catdir, prod):
    if prod in LEGACY:
        return f'/products/{LEGACY[prod][0]}/{PRODUCT_SLUG[prod]}'
    c = next(c for c in CATS if catdir in (c[0], c[2]))
    if prod in ('57xilie', 'magneticAngleEncoderChip'):
        c = CATS[0]
    return f'/products/{c[0]}/{PRODUCT_SLUG[prod]}'


def route_of(url):
    p = urllib.parse.urlparse(urllib.parse.urljoin(BASE, url))
    path = p.path.replace('/index.html', '').rstrip('/')
    m = re.match(r'/html/web/product/([^/]+)/([^/]+)$', path)
    if m and m.group(2) in PRODUCT_SLUG:
        return product_route(*m.groups())
    return None


def grid(table):
    """展开 rowspan/colspan，返回二维单元格列表（每格为 bs4 节点，被合并的格重复引用同一节点）。"""
    rows, pending = [], {}
    for tr in table.find_all('tr'):
        row, col = [], 0
        cells = tr.find_all(['td', 'th'], recursive=False)
        ci = 0
        while ci < len(cells) or col in pending:
            if col in pending:
                node, left = pending[col]
                row.append(node)
                if left <= 1:
                    del pending[col]
                else:
                    pending[col] = (node, left - 1)
                col += 1
                continue
            c = cells[ci]
            ci += 1
            span = int(c.get('colspan', 1) or 1)
            rs = int(c.get('rowspan', 1) or 1)
            for k in range(span):
                row.append(c)
                if rs > 1:
                    pending[col] = (c, rs - 1)
                col += 1
        rows.append(row)
    return rows


def clean_table(table):
    """规格参数表：保留结构，清理属性，图片本地化，表内“表头行”转 th。"""
    for t in table.select('.product-internal-table-head'):
        if t.name == 'tr':
            for td in t.find_all('td'):
                td.name = 'th'
        else:
            t.name = 'th'
    imgs = []
    for im in table.find_all('img'):
        if im.get('src'):
            im['src'] = asset(im['src'])
            imgs.append(im['src'])
    for t in table.find_all(True):
        for a in list(t.attrs):
            if a not in ('src', 'rowspan', 'colspan', 'alt'):
                del t.attrs[a]
        if t.name in ('span', 'font', 'strong', 'b'):
            t.unwrap()
    for p in table.find_all('p'):
        if p.find('img'):
            p.unwrap()
        else:
            p.insert_after(table.new_tag('br'))
            p.unwrap()
    for td in table.find_all(['td', 'th']):
        while td.contents and getattr(td.contents[-1], 'name', None) == 'br':
            td.contents[-1].extract()
        if not td.get_text(strip=True) and not td.find('img'):
            td.string = '—'
        im = td.find('img')
        if im and len(td.find_all(True)) >= 1 and not td.get_text(strip=True):
            td['class'] = 'ct-cell-img'
    # 表头：第一行都是 th 时包进 thead
    trs = table.find_all('tr')
    if trs and not table.find('thead') and all(c.name == 'th' for c in trs[0].find_all(['td', 'th'], recursive=False)):
        thead = table.new_tag('thead')
        trs[0].wrap(thead)
        table.insert(0, thead.extract())
    return str(table), imgs


def doc_records(tables):
    """技术文档表 → [{scene, series, type, cn, en}]，统一口径。"""
    recs = []
    for tb in tables:
        g = grid(tb)
        if not g:
            continue
        head = [text(c) for c in g[0]]
        idx = {k: i for i, k in enumerate(head)}
        for row in g[1:]:
            def cell(name):
                i = idx.get(name)
                return row[i] if i is not None and i < len(row) else None

            def fname(c):
                d = c.select_one('.free-product-technical-document') if c else None
                return d.get_text(strip=True) if d else ''
            recs.append(dict(scene=text(cell('应用场景')) or '通用', series=text(cell('产品系列')),
                             type=text(cell('文档类型')), cn=fname(cell('中文版')), en=fname(cell('英文版'))))
    out, seen = [], set()
    for r in recs:
        key = (r['scene'], r['series'], r['type'], r['cn'], r['en'])
        if key not in seen and (r['cn'] or r['en']):
            seen.add(key)
            out.append(r)
    for r in out:
        for k in ('cn', 'en'):
            if r[k]:
                ASSETS['/files/' + r[k]] = BASE + '/api/resource/freeDownload?name=' + urllib.parse.quote(r[k])
    return out


def extract_product(path):
    s = soup(path)
    pc = s.select_one('.product-content')
    for sel in ['.product-article-md', '.contact-us-md', '.product-technology-table-md', '.product-below-title']:
        for t in pc.select(sel):
            t.decompose()
    d = dict(source=path, kind=text(pc.select_one('.product-title')), intro=[], image='', highlights=[],
             highlights_title='', specs=[], figures=[], docs=[], videos=[], extra=[])
    for c in pc.find_all(recursive=False):
        cls = ' '.join(c.get('class') or [])
        subt = c.select_one('.product-subtitle')
        subtitle = text(subt).rstrip('：:') if subt else ''
        if subt:
            subt.decompose()
        if 'product-title' in cls:
            continue
        if 'product-introduction' in cls:
            im = c.select_one('.product-image img')
            d['image'] = asset(im['src']) if im else ''
            d['intro'] = lines(c.select_one('.product-article'))
        elif 'product-advantage' in cls:
            d['highlights_title'] = subtitle
            dets = c.select('.product-advantage-detail')
            items = [l for dd in dets for l in lines(dd)] if dets else lines(c)
            d['highlights'] = [re.sub(r'^[ㆍ·•・\-\s]+', '', x).strip() for x in items if x.strip('ㆍ·•・- ')]
        elif 'product-alternative' in cls:
            d['figures'] += [asset(im['src']) for im in c.find_all('img')]
        elif 'product-technology' in cls:
            d['docs'] = doc_records(c.find_all('table'))
        elif 'product-video' in cls:
            v = c.find('video')
            if v:
                d['videos'].append(dict(title=subtitle, src=asset(v['src'], 'videos'), poster=asset(v['poster']) if v.get('poster') else ''))
        elif c.find('table'):
            for tb in c.find_all('table'):
                h, imgs = clean_table(tb)
                d['specs'].append(h)
        elif c.get_text(strip=True) or c.find('img'):
            d['extra'].append(dict(title=subtitle, lines=lines(c), images=[asset(i['src']) for i in c.find_all('img') if i.get('src')]))
    return d


def extract_overview():
    s = soup('/html/web/product/magneticAngleDetectionChip/index.html')
    cats = []
    for (key, name, dirname), g in zip(CATS, s.select('.conntek-main .totalPart')):
        items = []
        for pd in g.select('.productDetail'):
            intro = pd.select_one('.product-introduction')
            href = intro.find('a')['href']
            prod = urllib.parse.urlparse(href).path.replace('/index.html', '').rstrip('/').split('/')[-1]
            img = pd.select_one('.productImg img')
            items.append(dict(prod=prod, slug=PRODUCT_SLUG[prod], route=product_route(key, prod),
                              title=text(intro.select_one('.product-title')),
                              summary=' '.join(lines(intro.select_one('.product-description'))),
                              image=asset(img['src']) if img else ''))
        cats.append(dict(key=key, name=name, dir=dirname, items=items))
    s2 = soup('/html/web/product/index.html')
    for c, b in zip(cats, s2.select('.list-overview .section-box')):
        c['cover'] = asset(b.find('img')['src'])
    return cats


def extract_apps():
    s = soup('/html/web/application/consumerElectronics/index.html')
    home = soup('/')
    covers = [asset(i['src']) for i in home.select('.section-application img')]
    sa = home.select_one('.section-application')
    typical, cur = {}, None
    names = [a[1] for a in APPS]
    for t in sa.get_text('\n', strip=True).split('\n'):
        if t in names:
            cur = t
            typical[cur] = []
        elif cur and t.upper() not in [a[3].upper() for a in APPS]:
            typical[cur].append(t)
    # 首页应用板块图片顺序：消费、智能交通、智能生活、工业（与文字顺序一致）
    order = [t for t in sa.get_text('\n', strip=True).split('\n') if t in names]
    cover_of = dict(zip(order, covers))
    out = []
    for (key, name, dirname, en), g in zip(APPS, s.select('.functionTotal')):
        cases = []
        for b in g.select('.function_box'):
            img = b.select_one('img')
            a = b.select_one('.fMore a')
            cases.append(dict(title=text(b.select_one('.fTitle')), chip=text(b.select_one('.fRecommend')),
                              image=asset(img['src']) if img else '', route=route_of(a['href']) if a else None))
        out.append(dict(key=key, name=name, en=en, cover=cover_of.get(name, ''), typical=typical.get(name, []), cases=cases))
    return out


def extract_services():
    m = soup('/html/web/magneticSimulationService/index.html').select_one('.conntek-main')
    return dict(
        strengths=[dict(title=text(b.select_one('.itemTitle')), icon=asset(b.find('img')['src'])) for b in m.select('.totalBox')],
        cases=[asset(i['src']) for i in m.find_all('img') if re.search(r'anli\d', i.get('src', ''))],
        services=[dict(title=text(it.select_one('.serviceTitle')), icon=asset(it.select_one('.servicePic2 img')['src']),
                       points=[re.sub(r'^\d+、', '', p.get_text(strip=True)) for p in it.select('.servicecontent p') if p.get_text(strip=True)])
                  for it in m.select('.service-item')])


def extract_techtalks():
    arts = []
    for p in ['/html/web/techTalk/index.html', '/html/web/techTalkC/techTalk1/index.html', '/html/web/techTalkC/techTalkLast/index.html']:
        s = BeautifulSoup(open(os.path.join(ROOT, 'cache', IDX['pages'][p]), encoding='utf-8').read(), 'html.parser')
        for box in s.select('.section-box'):
            mm = re.search(r"window.open\('([^']+)'", box.get('onclick', ''))
            im = box.select_one('img')
            arts.append(dict(title=text(box.select_one('.section-box-title')), summary=text(box.select_one('.section-box-summary')),
                             date=text(box.select_one('.section-box-bottom')), href=mm.group(1).replace('\\', '') if mm else '',
                             image=asset(im['src']) if im else ''))
    return arts


def extract_about():
    m = soup('/html/web/joinUs/index.html').select_one('.conntek-main')
    home = soup('/')
    ab = home.select_one('.section-about')
    about = max((t.get_text(strip=True) for t in ab.find_all(['p', 'div']) if not t.find(['p', 'div'])), key=len)
    what = max((t.get_text(strip=True) for t in m.find_all(['p', 'div']) if '昆泰芯微电子服务于' in t.get_text() and not t.find(['p', 'div'])), key=len)
    values = []
    for it in m.select('.value_part'):
        parts = [t for t in it.get_text('\n', strip=True).split('\n') if t]
        if len(parts) >= 3:
            values.append(dict(name=parts[0], en=parts[1], desc=parts[2]))
    adv = m.find(string=re.compile('核心研发人员均毕业于')).strip()
    q = home.select_one('.section-quality')
    quality = [t.lstrip('ㆍ') for t in q.get_text('\n', strip=True).split('\n') if t.startswith('ㆍ')]
    jobs = []
    for li in m.select('.chancecontain li'):
        f = [text(li.select_one(f'.d{i}')) for i in range(1, 6)]
        body = [p.get_text(strip=True) for p in li.select('.deta p') if p.get_text(strip=True)]
        jobs.append(dict(title=f[0], count=f[1], edu=f[2], city=f[3], date=f[4], body=body))
    photos = [asset(i['src']) for i in m.find_all('img') if re.search(r'suzhou|1621989445518', i.get('src', ''))]
    photos.append(asset(ab.find('img')['src']))
    qimg = q.find('img', src=re.compile('ktpz'))
    return dict(about=about, what=what, values=values, advantage=adv, quality=quality,
                quality_image=asset(qimg['src']) if qimg else '', jobs=jobs, photos=photos)


def extract_contact():
    m = soup('/html/web/contactUs/index.html').select_one('.conntek-main')
    blocks = []
    for it in m.select('li'):
        tt = it.get_text('\n', strip=True).split('\n')
        if tt and '/' in tt[0] and tt[0].endswith(':'):
            cn, en = (tt[0].rstrip(':').split('/', 1) + [''])[:2]
            blocks.append(dict(name=cn.strip(), en=en.strip(), items=tt[1:]))
    cities = []
    for a in m.find_all('a'):
        im = a.find('img')
        if im:
            parts = [t for t in a.get_text('\n', strip=True).split('\n') if t]
            cities.append(dict(name=parts[0], en=parts[1] if len(parts) > 1 else '', image=asset(im['src'])))
    return dict(blocks=blocks, cities=cities)


def extract_home():
    home = soup('/')
    v = home.select_one('.section-publicity video')
    asset('/template/1/conntekCompany/Images/logo.jpg')
    return dict(video=dict(src=asset(v['src'], 'videos'), poster=asset(v['poster'])) if v else None)


def main():
    cats = extract_overview()
    titles = {i['prod']: i['title'] for c in cats for i in c['items']}
    products, done = {}, set()
    for path in IDX['pages']:
        m = re.match(r'/html/web/product/([^/]+)/([^/]+)/index.html$', path)
        if not m or m.group(2) not in PRODUCT_SLUG:
            continue
        route = product_route(*m.groups())
        if route in done:
            continue
        done.add(route)
        p = extract_product(path)
        p['route'] = route
        p['slug'] = route.rsplit('/', 1)[-1]
        p['category'] = route.split('/')[2]
        p['title'] = titles.get(m.group(2)) or LEGACY.get(m.group(2), ('', p['kind']))[1]
        p['legacy'] = m.group(2) in LEGACY
        products[p['slug']] = p
    site = dict(categories=cats, products=products, applications=extract_apps(), services=extract_services(),
                techtalks=extract_techtalks(), about=extract_about(), contact=extract_contact(), home=extract_home())
    json.dump(site, open(os.path.join(ROOT, 'cache', 'site.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(ASSETS, open(os.path.join(ROOT, 'cache', 'assets.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('products', len(products), 'assets', len(ASSETS))


if __name__ == '__main__':
    main()
