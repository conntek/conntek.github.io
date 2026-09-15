import json, re, os, urllib.parse
from bs4 import BeautifulSoup, Comment
from markdownify import markdownify as mdf

BASE = 'https://www.conntek.com.cn'
d = json.load(open('index.json', encoding='utf-8'))
OUT = 'raw'
os.makedirs(OUT, exist_ok=True)
assets = {'img': {}, 'video': {}, 'file': {}}


def local_asset(src, cur, kind='img'):
    u = urllib.parse.urljoin(BASE + cur, src)
    p = urllib.parse.urlparse(u)
    if 'conntek.com.cn' not in p.netloc:
        return src
    path = urllib.parse.unquote(p.path)
    sub = re.sub(r'^/(template/1/conntekCompany|upload/1/cms/content)', '', path)
    local = ('/images' if kind == 'img' else '/videos') + re.sub(r'^/(Picture|videos|editor|images)', '', sub)
    assets[kind][local] = u
    return local


def file_link(name):
    name = name.strip()
    assets['file']['/files/' + name] = BASE + '/api/resource/freeDownload?name=' + urllib.parse.quote(name)
    return '/files/' + urllib.parse.quote(name)


def clean(m, cur):
    for t in m(['script', 'style', 'noscript']):
        t.decompose()
    for t in m.find_all(string=lambda x: isinstance(x, Comment)):
        t.extract()
    for sel in ['.product-article-md', '.contact-us-md', '.product-technology-table-md', '.section-box-title-md',
                '.visible-xs', '.visible-sm', '.page-turn', '.product-redline', '.redLine', '.subLine']:
        for t in m.select(sel):
            t.decompose()
    for t in m.find_all('img'):
        s = t.get('src') or t.get('data-src') or t.get('data-original')
        if s:
            t['src'] = local_asset(s, cur)
    for t in m.find_all('video'):
        if t.get('poster'):
            t['poster'] = local_asset(t['poster'], cur)
        if t.get('src'):
            t['src'] = local_asset(t['src'], cur, 'video')
    for t in m.select('.free-product-technical-document'):
        name = t.get_text(strip=True)
        t.name = 'a'
        t.attrs = {'href': file_link(name), 'target': '_blank'}
    for t in m.find_all(True):
        for a in list(t.attrs):
            if a not in ('src', 'href', 'poster', 'controls', 'rowspan', 'colspan', 'alt', 'target'):
                del t.attrs[a]
    return m


for path, fn in d['pages'].items():
    if path == '/html/web//index.html':
        continue
    s = BeautifulSoup(open(fn, encoding='utf-8').read(), 'html.parser')
    ban = s.select_one('.productBanner h1')
    m = s.select_one('.conntek-main') or s.body
    arts = []
    for box in m.select('.section-box'):
        mm = re.search(r"window.open\('([^']+)'", box.get('onclick', ''))
        t = box.select_one('.section-box-title')
        sm = box.select_one('.section-box-summary')
        dt = box.select_one('.section-box-bottom')
        im = box.select_one('img')
        arts.append(dict(title=t.get_text(strip=True) if t else '', summary=sm.get_text(strip=True) if sm else '',
                         date=dt.get_text(strip=True) if dt else '',
                         href=mm.group(1).replace('\\', '') if mm else '',
                         img=local_asset(im['src'], path) if im else ''))
    clean(m, path)
    tables = {}
    for i, t in enumerate(m.find_all('table')):
        key = f'TABLEPLACEHOLDER{i}X'
        tables[key] = str(t)
        t.replace_with(s.new_string(key))
    vids = {}
    for i, t in enumerate(m.find_all('video')):
        key = f'VIDEOPLACEHOLDER{i}X'
        vids[key] = str(t)
        t.replace_with(s.new_string(key))
    md = mdf(str(m), heading_style='ATX', bullets='-')
    for k, v in {**tables, **vids}.items():
        md = md.replace(k, '\n\n' + v + '\n\n')
    md = re.sub(r'\n{3,}', '\n\n', md)
    slug = re.sub(r'^/html/web/?', '', path).replace('/index.html', '').strip('/') or 'home'
    rec = dict(path=path, slug=slug, banner=ban.get_text(strip=True) if ban else '', arts=arts)
    os.makedirs(os.path.dirname(f'{OUT}/{slug}.md') or OUT, exist_ok=True)
    open(f'{OUT}/{slug}.md', 'w', encoding='utf-8').write(md)
    open(f'{OUT}/{slug}.json', 'w', encoding='utf-8').write(json.dumps(rec, ensure_ascii=False, indent=1))
json.dump(assets, open('assets.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print({k: len(v) for k, v in assets.items()})
