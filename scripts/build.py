"""从 cache/ 里抓下来的 conntek.com.cn 页面生成 VitePress 的 docs/ 目录。

用法：python scripts/build.py            # 生成 md + 资源清单
      python scripts/build.py --download # 顺带下载图片/视频/文件到 docs/public
"""
import json, re, os, sys, urllib.parse, urllib.request, html as htmllib
from bs4 import BeautifulSoup, Comment, NavigableString
from markdownify import markdownify as mdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://www.conntek.com.cn'
DOCS = os.path.join(ROOT, 'docs')
PUBLIC = os.path.join(DOCS, 'public')
IDX = json.load(open(os.path.join(ROOT, 'cache', 'index.json'), encoding='utf-8'))
ASSETS = {}  # local path -> remote url

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
# linearHallChip 不在产品总览里，是旧页面；放到开关芯片下
LEGACY = {'linearHallChip': ('switch', '线性霍尔芯片（旧版页面）')}
APPS = [
    ('consumer-electronics', '消费类电子', 'consumerElectronics', 'CONSUMER ELECTRONICS'),
    ('intelligent-life', '智能生活', 'intelligentLife', 'INTELLIGENT LIFE'),
    ('industry4', '工业4.0', 'industry4', 'INDUSTRIAL 4.0'),
    ('intelligent-transportation', '智能交通', 'intelligentTransportation', 'INTELLIGENT TRANSPORTATION'),
]


def soup(path):
    s = BeautifulSoup(open(os.path.join(ROOT, 'cache', IDX['pages'][path]), encoding='utf-8').read(), 'html.parser')
    for t in s(['script', 'style', 'noscript']):
        t.decompose()
    for t in s.find_all(string=lambda x: isinstance(x, Comment)):
        t.extract()
    return s


# ---------- 链接与资源 ----------
def route_of(url):
    """把站内页面 URL 映射到本地路由；站外或未知返回 None。"""
    p = urllib.parse.urlparse(urllib.parse.urljoin(BASE, url))
    if 'conntek.com.cn' not in p.netloc or p.netloc.startswith('en.'):
        return None
    path = p.path.replace('/index.html', '').rstrip('/')
    frag = p.fragment
    if path in ('', '/html/web'):
        return '/'
    m = re.match(r'/html/web/product(?:/([^/]+))?(?:/([^/]+))?$', path)
    if m:
        cat, prod = m.groups()
        if prod and prod in PRODUCT_SLUG:
            return product_route(cat, prod)
        if cat:
            c = next((c for c in CATS if c[2] == cat), None)
            return f'/products/{c[0]}/' if c else '/products/'
        return '/products/'
    m = re.match(r'/html/web/application(?:/([^/]+))?$', path)
    if m:
        a = next((a for a in APPS if a[2] == m.group(1)), None)
        return f'/applications/{a[0]}' if a else '/applications/'
    if path.startswith('/html/web/magneticSimulationService'):
        return '/services'
    if path.startswith('/html/web/techTalk'):
        return '/tech-talks'
    if path.startswith('/html/web/joinUs'):
        return {'1': '/about/#公司介绍', '2': '/about/#核心价值观', '3': '/about/#加入我们'}.get(frag, '/about/')
    if path.startswith('/html/web/contactUs'):
        return '/contact'
    return None


def product_route(cat_key_or_dir, prod):
    if prod in LEGACY:
        return f'/products/{LEGACY[prod][0]}/{PRODUCT_SLUG[prod]}'
    c = next((c for c in CATS if cat_key_or_dir in (c[0], c[2])), None)
    if prod in ('57xilie', 'magneticAngleEncoderChip'):
        c = CATS[0]
    return f'/products/{c[0]}/{PRODUCT_SLUG[prod]}'


def asset(src, kind):
    u = urllib.parse.urljoin(BASE + '/', src.strip())
    p = urllib.parse.urlparse(u)
    if not p.netloc:
        return src
    name = urllib.parse.unquote(p.path)
    if 'conntek.com.cn' not in p.netloc:
        name = '/ext/' + os.path.basename(name)
    name = re.sub(r'^/(template/1/conntekCompany/(Picture|Images|videos)|upload/1/cms/(content/editor|content|category))/', '', name)
    local = f'/{kind}/' + name.lstrip('/')
    ASSETS[local] = urllib.parse.urlunsplit(urllib.parse.urlsplit(u)._replace(path=urllib.parse.quote(urllib.parse.unquote(p.path))))
    return local


def doc_file(name):
    name = name.strip()
    local = '/files/' + name
    ASSETS[local] = BASE + '/api/resource/freeDownload?name=' + urllib.parse.quote(name)
    return '/files/' + urllib.parse.quote(name)


# ---------- HTML 片段清理 ----------
KEEP_ATTR = {'src', 'href', 'poster', 'controls', 'rowspan', 'colspan', 'alt', 'target'}


def tidy(node):
    for t in node.find_all('img'):
        s = t.get('src') or t.get('data-src')
        if s:
            t['src'] = asset(s, 'images')
        t['alt'] = (t.get('alt') or '').strip()
    for t in node.find_all('video'):
        if t.get('poster'):
            t['poster'] = asset(t['poster'], 'images')
        if t.get('src'):
            t['src'] = asset(t['src'], 'videos')
    for t in node.select('.free-product-technical-document'):
        name = t.get_text(strip=True)
        if not name:
            t.name = 'span'
            t.attrs = {}
            continue
        href = doc_file(name)
        if os.path.isdir(os.path.join(PUBLIC, 'files')) and not os.path.exists(os.path.join(PUBLIC, 'files', name)):
            t.name = 'span'
            t.attrs = {'class': 'doc-missing'}
            t.string = f'{name}（官网暂不可下载）'
            continue
        t.name = 'a'
        t.attrs = {'href': href, 'target': '_blank', 'class': 'doc-link'}
    for t in node.select('.product-internal-table-head'):
        if t.name == 'tr':
            for td in t.find_all('td'):
                td.name = 'th'
        elif t.name == 'td':
            t.name = 'th'
    for t in node.find_all('a'):
        r = route_of(t.get('href', '')) if t.get('href') and not t.get('href', '').startswith('/files/') else None
        if r:
            t['href'] = r
    for t in node.find_all(True):
        for a in list(t.attrs):
            if a not in KEEP_ATTR and not (a == 'class' and 'doc-link' in t.get('class', [])):
                del t.attrs[a]
    for t in node.find_all(['span', 'font']):
        t.unwrap()
    for td in node.find_all('td'):
        if not td.get_text(strip=True) and not td.find(['img', 'a']):
            td.clear()
            td.append('—')
    return node


def html_block(node):
    """输出成一段不含空行的 HTML，保证 markdown-it 把它当成一个整块。"""
    h = str(node)
    h = re.sub(r'>\s+<', '><', h)
    h = re.sub(r'\n\s*', ' ', h)
    h = h.replace('{{', '&#123;&#123;')
    return h


def to_md(node):
    md = mdf(str(node), heading_style='ATX', bullets='-')
    md = re.sub(r'[ \t]+\n', '\n', md)
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def text(node):
    return node.get_text(strip=True) if node else ''


def para_text(node):
    """保留 <br> 为换行的纯文本段落。"""
    if not node:
        return ''
    for br in node.find_all('br'):
        br.replace_with('\n')
    lines = [l.strip() for l in node.get_text().split('\n')]
    return '\n\n'.join(l for l in lines if l)


def md_escape(s):
    return s.replace('*', '\\*').replace('<', '&lt;')


def write(rel, content):
    fn = os.path.join(DOCS, rel)
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    open(fn, 'w', encoding='utf-8', newline='\n').write(content.rstrip() + '\n')


def fm(**kw):
    lines = ['---']
    for k, v in kw.items():
        if isinstance(v, str):
            v = json.dumps(v, ensure_ascii=False)
        lines.append(f'{k}: {v}')
    lines.append('---\n')
    return '\n'.join(lines)


def origin(path):
    # 不在页面上展示原网页链接
    return '\n'


# ---------- 产品总览 ----------
def build_product_overview():
    s = soup('/html/web/product/magneticAngleDetectionChip/index.html')
    groups = s.select('.conntek-main .totalPart')
    assert len(groups) == len(CATS), len(groups)
    cats = []
    for (key, name, dirname), g in zip(CATS, groups):
        items = []
        for pd in g.select('.productDetail'):
            intro = pd.select_one('.product-introduction')
            a = intro.find('a')
            href = a.get('href') if a else ''
            prod = urllib.parse.urlparse(href).path.replace('/index.html', '').rstrip('/').split('/')[-1]
            num = text(intro.select_one('.hidden-xs'))
            title = text(intro.select_one('.product-title'))
            desc = para_text(intro.select_one('.product-description'))
            img = pd.select_one('.productImg img')
            items.append(dict(num=num, title=title, desc=desc, prod=prod,
                              route=product_route(key, prod),
                              img=asset(img['src'], 'images') if img else ''))
        cats.append(dict(key=key, name=name, dir=dirname, items=items))
    # 类目封面图
    s2 = soup('/html/web/product/index.html')
    covers = [asset(b.find('img')['src'], 'images') for b in s2.select('.list-overview .section-box')]
    for c, cov in zip(cats, covers):
        c['cover'] = cov
    return cats


def card(route, img, title, desc='', badge=''):
    h = f'<a class="ct-card" href="{route}">'
    if img:
        h += f'<div class="ct-card-img"><img src="{img}" alt="{htmllib.escape(title)}"></div>'
    h += '<div class="ct-card-body">'
    if badge:
        h += f'<span class="ct-badge">{htmllib.escape(badge)}</span>'
    h += f'<h3>{htmllib.escape(title)}</h3>'
    if desc:
        d = desc.replace('\n\n', ' ')
        h += f'<p>{htmllib.escape(d)}</p>'
    h += '</div></a>'
    return h


def write_products(cats):
    out = fm(title='产品中心', outline=2)
    out += '# 产品中心\n\n'
    out += '昆泰芯产品覆盖 3D 霍尔、编码器、开关、信号调理与旋钮模组五大类。点击类目或产品卡片查看详情、规格参数与技术文档。\n\n'
    out += '<div class="ct-grid ct-grid-5">' + ''.join(
        card(f'/products/{c["key"]}/', c['cover'], c['name'], f'{len(c["items"])} 个产品系列') for c in cats) + '</div>\n\n'
    for c in cats:
        out += f'## {c["name"]}\n\n'
        out += '<div class="ct-grid">' + ''.join(card(i['route'], i['img'], i['title'], badge=i['num']) for i in c['items']) + '</div>\n\n'
    out += origin('/html/web/product/index.html')
    write('products/index.md', out)
    for c in cats:
        out = fm(title=c['name'])
        out += f'# {c["name"]}\n\n'
        for i in c['items']:
            out += f'## {md_escape(i["title"])}\n\n'
            out += f'<div class="ct-row"><div class="ct-row-img"><img src="{i["img"]}" alt=""></div><div class="ct-row-body">\n\n'
            out += md_escape(i['desc']) + f'\n\n[了解产品详情 →]({i["route"]})\n\n</div></div>\n\n'
        out += origin(f'/html/web/product/{c["dir"]}/index.html')
        write(f'products/{c["key"]}/index.md', out)


# ---------- 产品详情 ----------
def build_product_page(path, title, cat_key):
    s = soup(path)
    pc = s.select_one('.product-content')
    ptitle = text(pc.select_one('.product-title'))
    out = fm(title=title, description=ptitle, outline=2)
    out += f'# {md_escape(title)}\n\n'
    out += f'<p class="ct-subtitle">{htmllib.escape(ptitle)}</p>\n\n'
    for sel in ['.product-article-md', '.contact-us-md', '.product-technology-table-md', '.product-below-title', '.product-title']:
        for t in pc.select(sel):
            t.decompose()
    videos = []
    for c in pc.find_all(recursive=False):
        cls = ' '.join(c.get('class') or [])
        subt = c.select_one('.product-subtitle')
        subtitle = text(subt).rstrip('：:') if subt else ''
        if subt:
            subt.decompose()
        if 'product-introduction' in cls:
            img = c.select_one('.product-image img')
            art = c.select_one('.product-article')
            tidy(c)
            body = to_md(art) if art else ''
            if img:
                out += f'<div class="ct-hero"><div class="ct-hero-img"><img src="{img["src"]}" alt="{htmllib.escape(title)}"></div><div class="ct-hero-body">\n\n{body}\n\n<a class="ct-btn" href="/contact">联系我们</a>\n\n</div></div>\n\n'
            else:
                out += body + '\n\n'
        elif 'product-advantage' in cls:
            out += f'## {subtitle or "主要优势"}\n\n'
            dets = c.select('.product-advantage-detail')
            if dets:
                for dd in dets:
                    t = para_text(dd).lstrip('ㆍ·•・ ').strip()
                    if t:
                        out += '- ' + md_escape(t).replace('\n\n', '<br>') + '\n'
                out += '\n'
            else:
                tidy(c)
                md = to_md(c)
                md = re.sub(r'^[ㆍ·•・]\s*', '- ', md, flags=re.M)
                out += md + '\n\n'
        elif 'product-alternative' in cls:
            tidy(c)
            for im in c.find_all('img'):
                out += f'<p class="ct-figure"><img src="{im["src"]}" alt=""></p>\n\n'
        elif 'product-technology' in cls:
            out += f'## {subtitle or "技术文档"}\n\n'
            out += '::: tip 下载说明\n点击文件名直接打开（文件已随本站本地保存）；`.exe` 为上位机安装包。\n:::\n\n'
            tidy(c)
            for tb in c.find_all('table'):
                out += '<div class="ct-table">' + html_block(tb) + '</div>\n\n'
        elif 'product-video' in cls:
            tidy(c)
            v = c.find('video')
            if v:
                videos.append((subtitle, v))
        elif c.find('table'):
            out += f'## {subtitle or "规格参数"}\n\n'
            tidy(c)
            for tb in c.find_all('table'):
                out += '<div class="ct-table">' + html_block(tb) + '</div>\n\n'
        elif c.get_text(strip=True) or c.find('img'):
            if subtitle:
                out += f'## {subtitle}\n\n'
            tidy(c)
            md = to_md(c)
            md = re.sub(r'^[ㆍ·•・]\s*', '- ', md, flags=re.M)
            out += md + '\n\n'
    if videos:
        out += '## 视频\n\n'
        for sub, v in videos:
            out += f'### {sub}\n\n<video class="ct-video" controls preload="none" poster="{v.get("poster", "")}" src="{v["src"]}"></video>\n\n'
    out += origin(path)
    return out


# ---------- 市场应用 ----------
def build_applications():
    s = soup('/html/web/application/consumerElectronics/index.html')
    groups = s.select('.functionTotal')
    assert len(groups) == 4
    home = soup('/')
    idx = fm(title='市场应用') + '# 市场应用\n\n昆泰芯芯片落地的四大应用场景。\n\n<div class="ct-grid ct-grid-4">'
    scene_imgs = [asset(i['src'], 'images') for i in home.select('.section-application img')]
    for (key, name, dirname, en), g, simg in zip(APPS, groups, scene_imgs + [''] * 4):
        items = []
        for b in g.select('.function_box'):
            img = b.select_one('img')
            a = b.select_one('.fMore a')
            items.append(dict(title=text(b.select_one('.fTitle')), chip=text(b.select_one('.fRecommend')),
                              img=asset(img['src'], 'images') if img else '',
                              route=route_of(a['href']) if a else ''))
        out = fm(title=name) + f'# {name}\n\n<p class="ct-subtitle">{en}</p>\n\n'
        out += '| 应用 | 推荐芯片 |\n|---|---|\n' + ''.join(f'| {i["title"]} | [{i["chip"]}]({i["route"]}) |\n' for i in items) + '\n'
        out += '<div class="ct-grid ct-grid-app">' + ''.join(
            card(i['route'], i['img'], i['title'], badge=i['chip']) for i in items) + '</div>\n'
        out += origin(f'/html/web/application/{dirname}/index.html')
        write(f'applications/{key}.md', out)
        idx += card(f'/applications/{key}', simg, name, f'{en} · {len(items)} 个应用案例')
    idx += '</div>\n'
    # 首页应用板块里的场景文字
    sa = home.select_one('.section-application')
    idx += '\n## 典型场景\n\n'
    txt = sa.get_text('\n', strip=True).split('\n')
    names = [a[1] for a in APPS]
    ens = [a[3] for a in APPS]
    scenes, cur = {}, None
    for t in txt:
        if t in names:
            cur = t
            scenes.setdefault(cur, [])
        elif t in ens or t.upper() in ens:
            continue
        elif cur:
            scenes[cur].append(t)
    for name, items in scenes.items():
        if items:
            idx += f'- **{name}**：' + '、'.join(items) + '\n'
    idx += '\n' + origin('/html/web/application/index.html')
    write('applications/index.md', idx)


# ---------- 磁仿真 ----------
def build_services():
    s = soup('/html/web/magneticSimulationService/index.html')
    m = s.select_one('.conntek-main')
    out = fm(title='磁仿真&技术服务') + '# 磁仿真&技术服务\n\n<p class="ct-subtitle">MAGNETIC SIMULATION TECHNOLOGY SERVICE</p>\n\n'
    out += '## 核心优势\n\n懂结构、懂设计、懂磁路、懂电路。\n\n<div class="ct-grid ct-grid-3 ct-icons">'
    for it in m.select('.totalBox'):
        im = it.select_one('img')
        img = f'<img src="{asset(im["src"], "images")}" alt="">' if im else ''
        out += f'<div class="ct-icon-card">{img}<h3>{htmllib.escape(text(it.select_one(".itemTitle")))}</h3></div>'
    out += '</div>\n\n## 解决方案\n\n通过磁学仿真、磁路设计并与电路、结构低成本快速迭代，最终实现功能。\n\n'
    out += '<div class="ct-steps"><span>磁路设计</span><span>电路设计</span><span>结构设计</span><span>低成本快速迭代</span></div>\n\n'
    cases = [i for i in m.find_all('img') if re.search(r'anli\d', i.get('src', ''))]
    out += '<div class="ct-grid ct-grid-3">' + ''.join(
        f'<p class="ct-figure"><img src="{asset(i["src"], "images")}" alt="仿真案例"></p>' for i in cases) + '</div>\n\n'
    out += '## 服务内容\n\n'
    for it in m.select('.service-item'):
        title = text(it.select_one('.serviceTitle'))
        body = [p.get_text(strip=True) for p in it.select('.servicecontent p') if p.get_text(strip=True)]
        out += f'### {title}\n\n' + '\n'.join(f'{i+1}. {re.sub(r"^\d+、", "", b)}' for i, b in enumerate(body)) + '\n\n'
    out += origin('/html/web/magneticSimulationService/index.html')
    write('services.md', out)


# ---------- 技术洞见 ----------
def build_techtalks():
    arts = []
    for p in ['/html/web/techTalk/index.html', '/html/web/techTalkC/techTalk1/index.html', '/html/web/techTalkC/techTalkLast/index.html']:
        s = BeautifulSoup(open(os.path.join(ROOT, 'cache', IDX['pages'][p]), encoding='utf-8').read(), 'html.parser')
        for box in s.select('.section-box'):
            mm = re.search(r"window.open\('([^']+)'", box.get('onclick', ''))
            im = box.select_one('img')
            arts.append(dict(title=text(box.select_one('.section-box-title')), summary=text(box.select_one('.section-box-summary')),
                             date=text(box.select_one('.section-box-bottom')), href=mm.group(1).replace('\\', '') if mm else '',
                             img=asset(im['src'], 'images') if im else ''))
    out = fm(title='技术洞见', outline=2) + '# 技术洞见\n\n<p class="ct-subtitle">TECH TALKS · 共 ' + str(len(arts)) + ' 篇，文章链接指向微信公众号原文</p>\n\n'
    year = None
    for a in arts:
        y = a['date'][:4]
        if y != year:
            out += f'## {y} 年\n\n'
            year = y
        out += (f'<a class="ct-article" href="{a["href"]}" target="_blank"><img src="{a["img"]}" alt="">'
                f'<div><h3>{htmllib.escape(a["title"])}</h3><p>{htmllib.escape(a["summary"])}</p>'
                f'<time>{a["date"]}</time></div></a>\n\n')
    out += origin('/html/web/techTalk/index.html')
    write('tech-talks.md', out)


# ---------- 关于我们 ----------
def build_about():
    s = soup('/html/web/joinUs/index.html')
    m = s.select_one('.conntek-main')
    home = soup('/')
    about_home = home.select_one('.section-about')
    about_txt = max((p.get_text(strip=True) for p in about_home.find_all(['p', 'div']) if not p.find(['p', 'div'])), key=len)
    what = max((p.get_text(strip=True) for p in m.find_all(['p', 'div']) if '昆泰芯微电子服务于' in p.get_text() and not p.find(['p', 'div'])), key=len)
    out = fm(title='关于我们', outline=2) + '# 关于昆泰\n\n<p class="ct-subtitle">智能感知世界　传递美好生活 · smart sensing creates better life</p>\n\n'
    out += '## 公司介绍\n\n'
    out += '<div class="ct-stat"><b>2016</b><span>since</span></div>\n\n'
    out += about_txt + '\n\n' + '### What we do\n\n' + what + '\n\n'
    photos = [i for i in m.find_all('img') if re.search(r'suzhou|1621989445518', i.get('src', ''))]
    photos.append(about_home.find('img'))
    out += '<div class="ct-grid ct-grid-3">' + ''.join(f'<p class="ct-figure"><img src="{asset(i["src"], "images")}" alt="公司环境"></p>' for i in photos if i) + '</div>\n\n'
    out += '## 核心价值观\n\n| 价值观 | English | 释义 |\n|---|---|---|\n'
    for it in m.select('.value_part'):
        parts = [t for t in it.get_text('\n', strip=True).split('\n') if t]
        if len(parts) >= 3:
            out += f'| **{parts[0]}** | {parts[1].upper()} | {parts[2]} |\n'
    adv = m.find(string=re.compile('核心研发人员均毕业于'))
    out += '\n## 核心优势\n\n' + adv.strip().replace('。 公司', '。\n\n公司') + '\n\n'
    q = home.select_one('.section-quality')
    out += '## 品质认证\n\n'
    for t in q.get_text('\n', strip=True).split('\n'):
        if t.startswith('ㆍ'):
            out += '- ' + t.lstrip('ㆍ') + '\n'
    qimg = q.find('img', src=re.compile('ktpz'))
    if qimg:
        out += f'\n<p class="ct-figure"><img src="{asset(qimg["src"], "images")}" alt="品质认证"></p>\n'
    out += '\n## 加入我们\n\n招聘邮箱：[hr@conntek.com.cn](mailto:hr@conntek.com.cn)　电话：0512-62982283\n\n'
    out += '| 职位名称 | 人数 | 学历 | 工作地点 | 发布时间 |\n|---|---|---|---|---|\n'
    jobs = []
    for li in m.select('.chancecontain li'):
        f = [text(li.select_one(f'.d{i}')) for i in range(1, 6)]
        deta = li.select_one('.deta')
        jobs.append((f, deta))
        out += '| ' + ' | '.join(f) + ' |\n'
    out += '\n'
    for f, deta in jobs:
        body = ''
        if deta:
            for p in deta.find_all('p'):
                t = p.get_text(strip=True)
                if t:
                    body += t + '\n\n'
        body = re.sub(r'^(\d+)[\.、]\s*', r'\1. ', body, flags=re.M)
        body = re.sub(r'^(工作内容具体描述|岗位职责|任职资格描述|任职要求)[:：]\s*$', r'**\1**', body, flags=re.M)
        out += f'::: details {f[0]}（{f[3]} · {f[1]} 人）\n\n{body.strip()}\n\n:::\n\n'
    out += origin('/html/web/joinUs/index.html')
    write('about/index.md', out)


# ---------- 联系我们 ----------
def build_contact():
    s = soup('/html/web/contactUs/index.html')
    m = s.select_one('.conntek-main')
    out = fm(title='联系我们') + '# 联系我们\n\n'
    out += '<div class="ct-grid ct-grid-3 ct-contact">'
    for li in m.select('.contactContent') or []:
        pass
    blocks = []
    for it in m.select('li'):
        tt = it.get_text('\n', strip=True).split('\n')
        if tt and ('/' in tt[0] and tt[0].endswith(':')):
            blocks.append(tt)
    for tt in blocks:
        head = tt[0].rstrip(':')
        cn, en = (head.split('/', 1) + [''])[:2]
        rows = ''
        for t in tt[1:]:
            if '@' in t:
                rows += f'<li><a href="mailto:{t}">{t}</a></li>'
            elif re.fullmatch(r'[\d\-]+', t):
                rows += f'<li><a href="tel:{t}">{t}</a></li>'
            else:
                rows += f'<li>{htmllib.escape(t)}</li>'
        out += f'<div class="ct-contact-card"><h3>{htmllib.escape(cn)}</h3><small>{htmllib.escape(en)}</small><ul>{rows}</ul></div>'
    out += '</div>\n\n## 办公地点\n\n<div class="ct-grid ct-grid-4">'
    for a in m.find_all('a'):
        im = a.find('img')
        if not im:
            continue
        parts = [t for t in a.get_text('\n', strip=True).split('\n') if t]
        out += f'<div class="ct-city"><img src="{asset(im["src"], "images")}" alt=""><b>{parts[0]}</b><small>{parts[1] if len(parts) > 1 else ""}</small></div>'
    out += '</div>\n'
    out += origin('/html/web/contactUs/index.html')
    write('contact.md', out)


# ---------- 首页 ----------
def build_home(cats):
    home = soup('/')
    v = home.select_one('.section-publicity video')
    video = f'<video class="ct-video" controls preload="none" poster="{asset(v["poster"], "images")}" src="{asset(v["src"], "videos")}"></video>' if v else ''
    feats = ''
    for c in cats:
        names = '、'.join(re.split(r'[-—–]+\s*', i['title'])[-1].strip() for i in c['items'][:4])
        feats += f'  - title: {c["name"]}\n    details: {json.dumps(names, ensure_ascii=False)}\n    link: /products/{c["key"]}/\n'
    feats += '  - title: 磁仿真&技术服务\n    details: 可行性分析、传感器选型、磁路设计、量产良率优化\n    link: /services\n'
    out = f'''---
layout: home
title: 昆泰芯微电子
hero:
  name: 昆泰芯微电子
  text: 智能感知世界 传递美好生活
  tagline: 专注于面向物联网应用的传感器芯片研发、生产和销售 · smart sensing creates better life
  image:
    src: /images/logo.jpg
    alt: CONNTEK
  actions:
    - theme: brand
      text: 产品中心
      link: /products/
    - theme: alt
      text: 市场应用
      link: /applications/
    - theme: alt
      text: 技术洞见
      link: /tech-talks
features:
{feats}---

<div class="ct-home">

## 企业宣传

{video}

## 热门产品

<div class="ct-grid">{''.join(card(i['route'], i['img'], i['title']) for c in cats for i in c['items'][:3])}</div>

</div>
'''
    asset('/template/1/conntekCompany/Images/logo.jpg', 'images')
    write('index.md', out)


def build_sidebar(cats):
    prods = [{'text': '产品总览', 'link': '/products/'}]
    for c in cats:
        items = [{'text': c['name'] + ' · 总览', 'link': f'/products/{c["key"]}/'}]
        items += [{'text': re.sub(r'\s+', ' ', i['title']), 'link': i['route']} for i in c['items']]
        for prod, (ck, t) in LEGACY.items():
            if ck == c['key']:
                items.append({'text': t, 'link': product_route(ck, prod)})
        prods.append({'text': c['name'], 'collapsed': False, 'items': items})
    apps = [{'text': '应用总览', 'link': '/applications/'}] + [{'text': a[1], 'link': f'/applications/{a[0]}'} for a in APPS]
    json.dump({'products': prods, 'applications': apps}, open(os.path.join(DOCS, '.vitepress', 'sidebar.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)


def download():
    ok = fail = skip = 0
    for local, url in sorted(ASSETS.items()):
        fn = os.path.join(PUBLIC, local.lstrip('/'))
        if os.path.exists(fn) and os.path.getsize(fn) > 0:
            skip += 1
            continue
        os.makedirs(os.path.dirname(fn), exist_ok=True)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout=300) as r, open(fn + '.part', 'wb') as f:
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
            os.replace(fn + '.part', fn)
            ok += 1
            print('OK  ', local, os.path.getsize(fn), flush=True)
        except Exception as e:
            fail += 1
            print('FAIL', local, url, e, flush=True)
    print(f'downloaded {ok}, skipped {skip}, failed {fail}')


def main():
    os.makedirs(os.path.join(DOCS, '.vitepress'), exist_ok=True)
    cats = build_product_overview()
    write_products(cats)
    titles = {i['prod']: (c['key'], i['title']) for c in cats for i in c['items']}
    done = set()
    for path in IDX['pages']:
        m = re.match(r'/html/web/product/([^/]+)/([^/]+)/index.html$', path)
        if not m:
            continue
        catdir, prod = m.groups()
        route = product_route(catdir, prod)
        if route in done:
            continue
        done.add(route)
        if prod in titles:
            ck, title = titles[prod]
        else:
            ck, title = LEGACY[prod] if prod in LEGACY else (next(c[0] for c in CATS if c[2] == catdir), prod)
        write(route.lstrip('/') + '.md', build_product_page(path, title, ck))
    build_applications()
    build_services()
    build_techtalks()
    build_about()
    build_contact()
    build_home(cats)
    build_sidebar(cats)
    json.dump(ASSETS, open(os.path.join(ROOT, 'cache', 'assets.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    kinds = {}
    for k in ASSETS:
        kinds[k.split('/')[1]] = kinds.get(k.split('/')[1], 0) + 1
    print('assets:', kinds)
    if '--download' in sys.argv:
        download()


if __name__ == '__main__':
    main()
