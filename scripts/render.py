"""按统一模板把内容渲染成 docs/ 下的 md 页面。

数据来源（都在仓库内，可重复生成）：
  cache/site.json          scripts/extract.py 从原始 HTML 抽出的内容
  content/copy.json        改写后的文案（导语、要点、关键参数），缺失时退回原文
  content/figures.json     规格图片的判定与转写（表格图 → 文字表格），缺失时原样显示图片
  cache/img_manifest.json  scripts/images.py 生成的统一比例派生图

所有页面共用同一骨架：面包屑 → 标题 → 导语 → 关键数字 → 若干二级章节 → 底部行动区。
"""
import json, os, re, html, urllib.parse
from collections import OrderedDict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
PUB = os.path.join(DOCS, 'public')
SITE_BASE = os.environ.get('SITE_BASE', '/msite/')


def load(rel, default):
    p = os.path.join(ROOT, rel)
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else default


S = load('cache/site.json', {})
COPY = load('content/copy.json', {})
FIGS = load('content/figures.json', {})
IMG = load('cache/img_manifest.json', {})
CATS = S['categories']
PRODUCTS = S['products']
APPS = S['applications']
CAT_BY_KEY = {c['key']: c for c in CATS}
ITEM_BY_SLUG = {i['slug']: (c, i) for c in CATS for i in c['items']}
ORDER = [i['slug'] for c in CATS for i in c['items']] + [s for s in PRODUCTS if s not in ITEM_BY_SLUG]

E = html.escape


# ---------- 基础 ----------
def with_base(content):
    if SITE_BASE in ('', '/'):
        return content
    return re.sub(r'\b(href|src|poster)="/(?!/)', lambda m: f'{m.group(1)}="{SITE_BASE}', content)


def write(rel, content):
    fn = os.path.join(DOCS, rel)
    os.makedirs(os.path.dirname(fn), exist_ok=True)
    content = re.sub(r'\n{3,}', '\n\n', content).replace('µ', 'μ')
    open(fn, 'w', encoding='utf-8', newline='\n').write(with_base(content).strip() + '\n')


def fm(**kw):
    out = ['---']
    for k, v in kw.items():
        out.append(f'{k}: {json.dumps(v, ensure_ascii=False) if isinstance(v, str) else (str(v).lower() if isinstance(v, bool) else v)}')
    return '\n'.join(out) + '\n---\n\n'


def exists(site_path):
    return bool(site_path) and os.path.exists(os.path.join(PUB, urllib.parse.unquote(site_path).lstrip('/')))


def icon(name):
    for ext in ('webp', 'png'):
        p = f'/img/icons-web/{name}.{ext}'
        if exists(p):
            return p
    return ''


def product_visual(slug):
    return icon(slug) or IMG.get(f'prod/{slug}.webp') or IMG.get(f'hero/{slug}') or ''


def pc(slug):
    """某产品的文案（改写优先，缺省用原文推导）。"""
    p = PRODUCTS[slug]
    c = COPY.get('products', {}).get(slug, {})
    model = c.get('model') or re.sub(r'.*?([A-Z]{2,}[A-Za-z0-9]+(?:\s*系列)?)\s*$', r'\1', p['title']) or p['title']
    name = c.get('name') or p['kind']
    lead = c.get('lead') or (p['intro'][0][:60] + '…' if p['intro'] else '')
    overview = c.get('overview') or merge_lines(p['intro'])
    highlights = c.get('highlights') or [{'title': '', 'desc': h} for h in dict.fromkeys(p['highlights'])]
    return dict(model=model, name=name, lead=lead, overview=overview, highlights=highlights,
                chips=c.get('chips', []), applications=c.get('applications', []), selection_note=c.get('selection_note', ''))


def merge_lines(lines):
    out, buf = [], ''
    for l in lines:
        buf += l
        if re.search(r'[。！？；）)]$', l):
            out.append(buf)
            buf = ''
    if buf:
        out.append(buf)
    return out


def eyebrow(*crumbs):
    parts = []
    for text, link in crumbs:
        parts.append(f'<a href="{link}">{E(text)}</a>' if link else f'<span>{E(text)}</span>')
    return '<nav class="c-crumbs">' + '<i>/</i>'.join(parts) + '</nav>\n\n'


def header(crumbs, title, lead, stats=None, kicker=''):
    out = eyebrow(*crumbs)
    if kicker:
        out += f'<p class="c-kicker">{E(kicker)}</p>\n\n'
    out += f'# {title}\n\n'
    if lead:
        out += f'<p class="c-lead">{E(lead)}</p>\n\n'
    if stats:
        out += stat_row(stats)
    return out


def stat_row(stats):
    return '<div class="c-stats">' + ''.join(
        f'<div class="c-stat"><b>{E(str(s["value"]))}</b><span>{E(s["label"])}</span></div>' for s in stats) + '</div>\n\n'


def section(title, lead=''):
    out = f'## {title}\n\n'
    if lead:
        out += f'<p class="c-sec-lead">{E(lead)}</p>\n\n'
    return out


def card(href, media, title, desc='', kicker='', tags=(), media_kind='icon', more='', external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ''
    h = f'<a class="c-card" href="{href}"{tgt}>'
    if media:
        h += f'<div class="c-card__media c-media--{media_kind}"><img src="{media}" alt="" loading="lazy"></div>'
    h += '<div class="c-card__body">'
    if kicker:
        h += f'<span class="c-card__kicker">{E(kicker)}</span>'
    h += f'<h3>{E(title)}</h3>'
    if desc:
        h += f'<p>{E(desc)}</p>'
    if tags:
        h += '<div class="c-tags">' + ''.join(f'<span>{E(t)}</span>' for t in tags) + '</div>'
    if more:
        h += f'<span class="c-card__more">{E(more)}</span>'
    h += '</div></a>'
    return h


def grid(cards, cols=3):
    return f'<div class="c-grid c-grid--{cols}">' + ''.join(cards) + '</div>\n\n'


def cta(title='需要选型建议、样品或技术支持？', text='昆泰芯提供芯片选型、磁场仿真与方案设计支持，欢迎与我们的销售和技术团队联系。',
        buttons=(('联系我们', '/contact'), ('sales@conntek.com.cn', 'mailto:sales@conntek.com.cn'),
                 ('support@conntek.com.cn', 'mailto:support@conntek.com.cn'))):
    btns = ''.join(f'<a class="c-btn{" c-btn--brand" if i == 0 else ""}" href="{href}">{E(label)}</a>' for i, (label, href) in enumerate(buttons))
    return (f'<div class="c-cta"><div><h2 class="c-cta__title">{E(title)}</h2><p>{E(text)}</p></div>'
            f'<div class="c-cta__actions">{btns}</div></div>\n')


def page_copy(key):
    return COPY.get('pages', {}).get(key, {})


# 栏目名全站只有一套（导航、面包屑、首页区块、页面标题共用）
SEC = {'products': '产品中心', 'applications': '市场应用', 'services': '磁仿真&技术服务', 'techtalks': '技术洞见',
       'about': '关于昆泰', 'contact': '联系我们', **COPY.get('section_names', {})}
BRAND = '昆泰芯微电子'
HOME = ('首页', '/')
# 由图片转写、且与 HTML 规格表数据有出入的参数图（content/figures.json 的 note 中已标注）
CONFLICT_FIGS = {'/images/microPowerSeriesAlter.png', '/images/hshrMagneticCodedAngleSensorAlter2.png'}


# ---------- 规格表 ----------
DECOR = {'/images/add.png', '/images/sub.png'}


def clean_spec(tbl_html):
    t = tbl_html
    for d in DECOR:
        t = re.sub(r'<img[^>]*src="' + re.escape(d) + r'"[^>]*/?>', '', t)
    # 规格表里的图（感应方向等）：限制尺寸，加说明
    def img_cell(m):
        src = m.group(1)
        f = FIGS.get(src, {})
        if f.get('kind') == 'decorative':
            return ''
        cap = f.get('caption', '')
        return f'<figure class="c-cell-fig"><img src="{src}" alt="{E(cap)}" loading="lazy">' + (f'<figcaption>{E(cap)}</figcaption>' if cap else '') + '</figure>'
    t = re.sub(r'<img[^>]*src="([^"]+)"[^>]*/?>', img_cell, t)
    t = re.sub(r'<td([^>]*)>\s*</td>', r'<td\1>—</td>', t)
    t = re.sub(r'>\s+<', '><', t)
    cols = max((len(re.findall(r'<t[hd]', r)) for r in re.findall(r'<tr.*?</tr>', t, re.S)), default=0)
    wide = ' c-table--wide' if cols >= 10 else ''
    return f'<div class="c-table{wide}">' + t.replace('\n', ' ') + '</div>\n\n'


def fig_table(f):
    tb = f['table']
    head = tb.get('header') or []
    rows = tb.get('rows') or []
    ncols = max([len(r) for r in head + rows] or [0])
    merge = tb.get('merge')
    out = '<div class="c-table"><table>'
    if head:
        out += '<thead>' + ''.join('<tr>' + ''.join(f'<th>{E(str(c))}</th>' for c in r) + '</tr>' for r in head) + '</thead>'
    out += '<tbody>'
    # 竖向相同值合并（只合并前两列）
    spans = [[1] * ncols for _ in rows]
    if merge:
        for ci in range(min(2, ncols)):
            r = 0
            while r < len(rows):
                k = r + 1
                while k < len(rows) and ci < len(rows[k]) and ci < len(rows[r]) and rows[k][ci] == rows[r][ci] and all(
                        rows[k][j] == rows[r][j] for j in range(ci)):
                    spans[k][ci] = 0
                    k += 1
                spans[r][ci] = k - r
                r = k
    for ri, r in enumerate(rows):
        out += '<tr>'
        for ci, c in enumerate(r):
            sp = spans[ri][ci] if ci < ncols else 1
            if sp == 0:
                continue
            rs = f' rowspan="{sp}"' if sp > 1 else ''
            out += f'<td{rs}>{E(str(c))}</td>'
        out += '</tr>'
    out += '</tbody></table></div>\n\n'
    title = tb.get('title') or f.get('caption')
    return (f'<p class="c-table-title">{E(title)}</p>\n\n' if title else '') + out


SPECS = load('content/specs.json', {})


def cell_html(v):
    v = str(v)
    return '<br>'.join(E(x) for x in v.split('\n'))


ID_COLS = ('完整型号', '型号', '产品型号', '产品名称')


def id_index(cols):
    for name in ID_COLS:
        if name in cols:
            return cols.index(name)
    return 0


def notes_html(t):
    return ''.join(f'<p class="c-note">{E(n)}</p>\n\n' for n in t.get('notes') or [])


def transposed_table(cols, rows, merge):
    """列多行少：参数竖排、型号横排，正好铺满一屏宽度。"""
    idc = id_index(cols)
    heads = [rows[r][idc] for r in range(len(rows))]
    out = '<div class="c-table c-table--t"><table><thead><tr><th>参数</th>' + ''.join(f'<th class="c-mono">{cell_html(h)}</th>' for h in heads) + '</tr></thead><tbody>'
    for ci, name in enumerate(cols):
        if ci == idc:
            continue
        vals = [rows[r][ci] for r in range(len(rows))]
        if all(v == vals[0] for v in vals) and len(vals) > 1:
            out += f'<tr><th>{E(name)}</th><td colspan="{len(vals)}">{cell_html(vals[0])}</td></tr>'
        else:
            out += f'<tr><th>{E(name)}</th>' + ''.join(f'<td>{cell_html(v)}</td>' for v in vals) + '</tr>'
    return out + '</tbody></table></div>\n\n'


def model_cards(cols, rows, merge):
    """列多行也多：每个型号一张参数卡，纵向阅读，不需要左右滑动。"""
    idc = id_index(cols)
    badge_cols = [c for c in merge if c != idc]
    out = '<div class="c-models">'
    for row in rows:
        badges = ''.join(f'<span>{E(cols[c])} {cell_html(row[c])}</span>' for c in badge_cols if str(row[c]).strip() not in ('', '—'))
        items = ''
        for ci, name in enumerate(cols):
            if ci == idc or ci in badge_cols:
                continue
            v = str(row[ci]).strip()
            if v in ('', '—'):
                continue
            items += f'<div><dt>{E(name)}</dt><dd>{cell_html(row[ci])}</dd></div>'
        out += (f'<article class="c-model"><header><h4>{cell_html(row[idc])}</h4>'
                + (f'<div class="c-tags">{badges}</div>' if badges else '') + f'</header><dl>{items}</dl></article>')
    return out + '</div>\n\n'


def full_table_details(cols, rows, merge):
    """完整表格（含全部列）折叠收起，需要逐列对照时再展开。"""
    out = '<details class="c-more"><summary>完整参数表（全部 %d 列）</summary>\n\n<div class="c-table c-table--wide"><table><thead><tr>' % len(cols)
    out += ''.join(f'<th>{E(c)}</th>' for c in cols) + '</tr></thead><tbody>'
    for row in rows:
        out += '<tr>' + ''.join(f'<td{" class=\'c-mono\'" if ci == id_index(cols) else ""}>{cell_html(v)}</td>' for ci, v in enumerate(row)) + '</tr>'
    return out + '</tbody></table></div>\n\n</details>\n\n'


def spec_entry(t):
    """content/specs.json 的一张表：matrix 为型号矩阵，keyvalue 为参数两两成对的四列表。"""
    out = f'<p class="c-table-title">{E(t["title"])}</p>\n\n' if t.get('title') and t['title'] != '规格参数' else ''
    if t.get('layout') == 'keyvalue':
        items = t.get('items') or []
        out += '<div class="c-table c-kv"><table><tbody>'
        for i in range(0, len(items), 2):
            out += '<tr>'
            for k, v in items[i:i + 2]:
                out += f'<th>{E(k)}</th><td>{cell_html(v)}</td>'
            if len(items[i:i + 2]) == 1:
                out += '<th></th><td></td>'
            out += '</tr>'
        out += '</tbody></table></div>\n\n'
    else:
        cols, rows = t.get('columns') or [], t.get('rows') or []
        g = t.get('group_by')
        merge = sorted(set((t.get('merge_cols') or []) + ([g] if isinstance(g, int) else [])))
        # 宽表不再横向滚动：列少直接排；列多行少转置；列多行也多改成逐型号参数卡
        if len(cols) > 8:
            if len(rows) <= 6:
                return out + transposed_table(cols, rows, merge) + full_table_details(cols, rows, merge) + notes_html(t)
            cards = model_cards(cols, rows, merge)
            if len(rows) > 12:   # 型号很多时先收起，避免页面过长
                cards = ('<details class="c-more c-more--cards"><summary>逐型号参数（'
                         + f'{len(rows)} 个型号）</summary>\n\n' + cards + '</details>\n\n')
            return out + cards + full_table_details(cols, rows, merge) + notes_html(t)
        out += '<div class="c-table"><table><thead><tr>' + ''.join(f'<th>{E(c)}</th>' for c in cols) + '</tr></thead><tbody>'
        # 纵向合并：相同值且同一分组内才合并
        spans = [[1] * len(cols) for _ in rows]
        for ci in merge:
            # 只受分组列（如“等级”）约束，不受其他合并列约束，以还原原表的合并方式
            before = [g] if isinstance(g, int) and g != ci else []
            r = 0
            while r < len(rows):
                k = r + 1
                while k < len(rows) and rows[k][ci] == rows[r][ci] and all(rows[k][b] == rows[r][b] for b in before):
                    k += 1
                spans[r][ci] = k - r
                for x in range(r + 1, k):
                    spans[x][ci] = 0
                r = k
        for ri, row in enumerate(rows):
            out += '<tr>'
            for ci, v in enumerate(row):
                sp = spans[ri][ci] if ci < len(cols) else 1
                if sp == 0:
                    continue
                classes = []
                if ci in merge:
                    classes.append('c-group')
                if cols and ci < len(cols) and cols[ci] in ('型号', '完整型号'):
                    classes.append('c-mono')
                attr = (f' rowspan="{sp}"' if sp > 1 else '') + (f' class="{" ".join(classes)}"' if classes else '')
                out += f'<td{attr}>{cell_html(v)}</td>'
            out += '</tr>'
        out += '</tbody></table></div>\n\n'
    for n in t.get('notes') or []:
        out += f'<p class="c-note">{E(n)}</p>\n\n'
    return out


def figures_for(slug, paths):
    """figures：表格图转文字表格，示意图保留，装饰/张冠李戴的丢弃。"""
    tables, diagrams = [], []
    for pth in paths:
        f = FIGS.get(pth)
        if f and slug not in f.get('used_by', [slug]):
            continue
        if f and f.get('mismatch') and slug in f.get('mismatch'):
            continue
        if f and f.get('kind') == 'decorative':
            continue
        if f and f.get('kind') == 'table' and f.get('table'):
            tables.append(fig_table(f))
        else:
            diagrams.append((pth, (f or {}).get('caption', '')))
    return tables, diagrams


# ---------- 技术文档 ----------
def file_cell(name):
    if not name:
        return '<span class="c-muted">—</span>'
    if not exists('/files/' + name):
        return f'<span class="c-muted" title="官网暂不可下载">{E(name)}（暂不可下载）</span>'
    ext = name.rsplit('.', 1)[-1].upper()
    return f'<a class="c-file" href="/files/{urllib.parse.quote(name)}" target="_blank"><em>{ext}</em>{E(name)}</a>'


def docs_table(docs):
    if not docs:
        return ''
    show_scene = any(d['scene'] != '通用' for d in docs)
    out = '<div class="c-table c-docs"><table><thead><tr>' + ('<th>适用</th>' if show_scene else '') + \
          '<th>型号</th><th>类型</th><th>中文版</th><th>英文版</th></tr></thead><tbody>'
    scenes = OrderedDict()
    for d in docs:
        scenes.setdefault(d['scene'], []).append(d)
    for scene, rows in scenes.items():
        for i, d in enumerate(rows):
            out += '<tr>'
            if show_scene and i == 0:
                out += f'<td rowspan="{len(rows)}" class="c-docs__scene">{E(scene)}</td>'
            out += f'<td class="c-mono">{E(d["series"])}</td><td><span class="c-badge">{E(d["type"])}</span></td>'
            out += f'<td>{file_cell(d["cn"])}</td><td>{file_cell(d["en"])}</td></tr>'
    return out + '</tbody></table></div>\n\n'


def video_grid(slug, videos):
    out = '<div class="c-grid c-grid--2">'
    for n, v in enumerate(videos):
        poster = IMG.get(f'poster/{slug}/{n}') or v.get('poster', '')
        out += (f'<figure class="c-video"><video controls preload="none" poster="{poster}" src="{v["src"]}"></video>'
                f'<figcaption>{E(v["title"])}</figcaption></figure>')
    return out + '</div>\n\n'


def chips_block(chips):
    if not chips:
        return ''
    return '<div class="c-specs">' + ''.join(
        f'<div class="c-spec"><b>{E(c["value"])}</b><span>{E(c["label"])}</span></div>' for c in chips) + '</div>\n\n'


# 原站个别案例的「了解详情」链接挂错产品：按推荐芯片型号纠正（见 content/conflicts.md）
CHIP_ROUTE = {'KTH564X': '/products/switch/linear-hall'}


def case_route(cse):
    return CHIP_ROUTE.get(cse['chip'].upper(), cse['route'])


def related_cases(route):
    out = []
    for a in APPS:
        for n, cse in enumerate(a['cases']):
            if case_route(cse) == route:
                out.append((a, n, cse))
    return out


# ---------- 产品详情 ----------
def cat_slugs(key):
    c = CAT_BY_KEY[key]
    return [i['slug'] for i in c['items']] + [s for s, p in PRODUCTS.items() if p['category'] == key and s not in ITEM_BY_SLUG]


def render_product(slug):
    p = PRODUCTS[slug]
    c = pc(slug)
    cat = CAT_BY_KEY[p['category']]
    out = fm(title=f'{c["model"]} {c["name"]}', description=c['lead'], aside=False, pageClass='c-page c-page--product')
    out += eyebrow(HOME, (SEC['products'], '/products/'), (cat['name'], f'/products/{cat["key"]}/'), (c['model'], None))
    out += '<div class="c-product-hero"><div class="c-product-hero__text">\n\n'
    out += f'<p class="c-kicker">{E(c["model"])}</p>\n\n# {c["name"]}\n\n<p class="c-lead">{E(c["lead"])}</p>\n\n'
    out += chips_block(c['chips'])
    n_docs = sum(1 for d in p['docs'] for k in ('cn', 'en') if d[k] and exists('/files/' + d[k]))
    if n_docs:
        out += f'<div class="c-actions"><a class="c-btn c-btn--brand" href="#技术文档">下载技术文档<small>{n_docs}</small></a>'
    else:
        out += '<div class="c-actions"><a class="c-btn c-btn--brand" href="/contact">索取产品资料</a>'
    out += '<a class="c-btn" href="/contact">申请样品 / 咨询</a></div>\n\n'
    hero = icon(slug) or IMG.get(f'hero/{slug}') or p['image']
    out += f'</div><div class="c-product-hero__media"><img src="{hero}" alt="{E(c["model"])}"></div></div>\n\n'

    out += section('产品概述')
    photo = IMG.get(f'photo/{slug}') or IMG.get(f'hero/{slug}')
    body = '\n\n'.join(c['overview'])
    if c['applications']:
        body += '\n\n<div class="c-tags c-tags--lg"><b>典型应用</b>' + ''.join(f'<span>{E(a)}</span>' for a in c['applications']) + '</div>'
    if photo:
        out += f'<div class="c-split c-split--overview"><div class="c-split__text">\n\n{body}\n\n</div><div class="c-split__media c-split__media--frame"><img src="{photo}" alt="{E(c["model"])} 产品图" loading="lazy"></div></div>\n\n'
    else:
        out += body + '\n\n'

    if c['highlights']:
        out += section('核心特点')
        out += '<div class="c-features">'
        for n, h in enumerate(c['highlights'], 1):
            t = h.get('title', '')
            out += f'<div class="c-feature"><span class="c-feature__no">{n:02d}</span><div>' + (f'<h3>{E(t)}</h3>' if t else '') + f'<p>{E(h["desc"])}</p></div></div>'
        out += '</div>\n\n'

    for x in p['extra']:
        imgs = [i for i in x['images'] if i not in DECOR]
        if imgs:
            out += section('产品形态', '千钮千态：可厚可薄、可大可小，模块化安装。')
            out += '<div class="c-gallery c-gallery--posters">' + ''.join(
                f'<a href="{i}" target="_blank"><img src="{i}" alt="" loading="lazy"></a>' for i in imgs) + '</div>\n\n'

    tables, diagrams = figures_for(slug, p['figures'])
    spec_html = ''
    for t in SPECS.get(slug) or []:
        spec_html += spec_entry(t)
        diagrams += [(f['src'], f.get('caption', '')) for f in t.get('figures', []) if f['src'] not in [d for d, _ in diagrams]]
    if not SPECS.get(slug):
        for s in p['specs']:
            if re.sub(r'<[^>]+>', '', s).strip():
                spec_html += clean_spec(s)
    if tables:
        conflict = any(f in CONFLICT_FIGS for f in p['figures'])
        label = '原站参数图（文字版' + (' · 与上表数据有出入，以产品手册为准' if conflict else '') + '）'
        spec_html += f'<details class="c-more"><summary>{label}</summary>\n\n' + ''.join(tables) + '</details>\n\n'
    if diagrams:
        spec_html += '<div class="c-figs">' + ''.join(
            f'<figure class="c-fig"><img src="{d}" alt="{E(cap)}" loading="lazy">' + (f'<figcaption>{E(cap)}</figcaption>' if cap else '') + '</figure>'
            for d, cap in diagrams) + '</div>\n\n'
    if spec_html.strip():
        out += section('规格参数', c['selection_note']) + spec_html

    if p['docs']:
        out += section('技术文档', '产品手册、评估套件说明与上位机软件，点击文件名直接下载。')
        out += docs_table(p['docs'])
    if p['videos']:
        out += section('视频资料')
        out += video_grid(slug, p['videos'])

    rel = related_cases(p['route'])
    if rel:
        out += section('应用案例', f'以下场景推荐使用 {c["model"]}。')
        out += grid([card(f'/applications/{a["key"]}', IMG.get(f'case/{a["key"]}/{n}'), cse['title'], kicker=a['name'], media_kind='photo')
                     for a, n, cse in rel[:8]], 4)

    siblings = [s for s in cat_slugs(cat['key']) if s != slug]
    if siblings:
        out += section('同类产品', f'{cat["name"]}产品线的其他系列。')
        out += grid([product_card(s) for s in siblings[:4]], 4)
    else:
        out += section('其他产品线', '浏览昆泰芯的其他产品线。')
        out += grid([category_card(x) for x in CATS if x['key'] != cat['key']], 4)
    out += cta()
    write(p['route'].lstrip('/') + '.md', out)


def product_card(slug, cols_desc=True):
    c = pc(slug)
    return card(PRODUCTS[slug]['route'], product_visual(slug), c['name'], c['lead'] if cols_desc else '', kicker=c['model'],
                media_kind='icon' if icon(slug) else 'product', more='查看详情')


def category_card(c, more='浏览产品线'):
    return card(f'/products/{c["key"]}/', icon('cat-' + c['key']) or IMG.get('cat/' + c['key']), c['name'],
                COPY.get('categories', {}).get(c['key'], {}).get('lead', ''), kicker=f'{len(cat_slugs(c["key"]))} 个系列',
                media_kind='icon' if icon('cat-' + c['key']) else 'photo', more=more)


def app_card(a, more='查看案例'):
    return card(f'/applications/{a["key"]}', icon('app-' + a['key']) or IMG.get(f'case/{a["key"]}/0'), a['name'],
                COPY.get('applications', {}).get(a['key'], {}).get('lead', ''), kicker=f'{len(a["cases"])} 个案例',
                media_kind='icon' if icon('app-' + a['key']) else 'photo', more=more)


# ---------- 产品中心 / 类目 ----------
def render_products():
    pcp = page_copy('products')
    n_docs = sum(1 for p in PRODUCTS.values() for d in p['docs'] for k in ('cn', 'en') if d[k] and exists('/files/' + d[k]))
    stats = [dict(value=len(CATS), label='产品线'), dict(value=len(PRODUCTS), label='产品系列'),
             dict(value=n_docs, label='份技术文档'), dict(value=sum(len(p['videos']) for p in PRODUCTS.values()), label='个产品视频')]
    out = fm(title=SEC['products'], description=pcp.get('lead', ''), aside=False, pageClass='c-page')
    out += header([HOME, (SEC['products'], None)], SEC['products'],
                  pcp.get('lead', '覆盖 3D 霍尔、磁编码器、磁开关、信号调理与旋钮模组的完整磁传感产品线。'), stats, kicker=BRAND)
    out += section('五大产品线')
    out += grid([category_card(c) for c in CATS], 5)
    for c in CATS:
        cc = COPY.get('categories', {}).get(c['key'], {})
        out += section(c['name'], cc.get('desc', ''))
        out += grid([product_card(s) for s in cat_slugs(c['key'])], 4)
    out += cta()
    write('products/index.md', out)

    for c in CATS:
        cc = COPY.get('categories', {}).get(c['key'], {})
        slugs = cat_slugs(c['key'])
        docs = sum(1 for s in slugs for d in PRODUCTS[s]['docs'] for k in ('cn', 'en') if d[k] and exists('/files/' + d[k]))
        out = fm(title=c['name'], description=cc.get('lead', ''), aside=False, pageClass='c-page')
        out += header([HOME, (SEC['products'], '/products/'), (c['name'], None)], c['name'], cc.get('lead', ''),
                      [dict(value=len(slugs), label='产品系列'), dict(value=docs, label='份技术文档'),
                       dict(value=sum(len(PRODUCTS[s]['videos']) for s in slugs), label='个产品视频')], kicker=SEC['products'])
        out += section('产品系列', cc.get('desc', ''))
        rows = ''
        for s in slugs:
            p = pc(s)
            rows += (f'<a class="c-row" href="{PRODUCTS[s]["route"]}"><div class="c-row__media c-media--{"icon" if icon(s) else "product"}">'
                     f'<img src="{product_visual(s)}" alt="" loading="lazy"></div><div class="c-row__body">'
                     f'<span class="c-card__kicker">{E(p["model"])}</span><h3>{E(p["name"])}</h3><p>{E(p["lead"])}</p>')
            if p['chips']:
                rows += '<div class="c-minispecs">' + ''.join(f'<span><b>{E(x["value"])}</b>{E(x["label"])}</span>' for x in p['chips']) + '</div>'
            rows += '<span class="c-card__more">查看详情</span></div></a>'
        out += f'<div class="c-rows">{rows}</div>\n\n'
        cases = [(a, n, cse) for s in slugs for a, n, cse in related_cases(PRODUCTS[s]['route'])]
        if cases:
            out += section('应用案例', f'采用{c["name"]}的终端产品。')
            seen, cards = set(), []
            for a, n, cse in cases:
                if cse['title'] in seen:
                    continue
                seen.add(cse['title'])
                cards.append(card(f'/applications/{a["key"]}', IMG.get(f'case/{a["key"]}/{n}'), cse['title'], kicker=cse['chip'], media_kind='photo'))
            out += grid(cards[:8], 4)
        out += section('其他产品线')
        out += grid([category_card(x) for x in CATS if x['key'] != c['key']], 4)
        out += cta()
        write(f'products/{c["key"]}/index.md', out)


# ---------- 市场应用 ----------
def render_applications():
    apc = page_copy('applications')
    total = sum(len(a['cases']) for a in APPS)
    chips = {cse['chip'] for a in APPS for cse in a['cases']}
    out = fm(title=SEC['applications'], description=apc.get('lead', ''), aside=False, pageClass='c-page')
    out += header([HOME, (SEC['applications'], None)], SEC['applications'],
                  apc.get('lead', '从消费电子到工业与交通，昆泰芯芯片已落地于众多终端产品。'),
                  [dict(value=len(APPS), label='应用领域'), dict(value=total, label='应用案例'), dict(value=len(chips), label='款推荐芯片')], kicker=BRAND)
    out += section('四大应用领域')
    out += grid([app_card(a) for a in APPS], 4)
    out += section('典型场景', '各领域中常见的磁传感需求。')
    out += '<div class="c-scenes">'
    for a in APPS:
        items = a['typical'] or [c['title'] for c in a['cases']]
        out += f'<a class="c-scene" href="/applications/{a["key"]}"><h3>{E(a["name"])}</h3><div class="c-tags">' + ''.join(f'<span>{E(t)}</span>' for t in items) + '</div></a>'
    out += '</div>\n\n' + cta()
    write('applications/index.md', out)

    for a in APPS:
        ac = COPY.get('applications', {}).get(a['key'], {})
        chips = OrderedDict()
        for cse in a['cases']:
            chips.setdefault((cse['chip'], case_route(cse)), []).append(cse['title'])
        out = fm(title=a['name'], description=ac.get('lead', ''), aside=False, pageClass='c-page')
        out += header([HOME, (SEC['applications'], '/applications/'), (a['name'], None)], a['name'], ac.get('lead', ''),
                      [dict(value=len(a['cases']), label='应用案例'), dict(value=len(chips), label='款推荐芯片')], kicker=SEC['applications'])
        out += section('应用案例', ac.get('desc', ''))
        out += grid([card(case_route(cse) or '/products/', IMG.get(f'case/{a["key"]}/{n}'), cse['title'], kicker=cse['chip'],
                          media_kind='photo', more='推荐芯片') for n, cse in enumerate(a['cases'])], 4)
        out += section('推荐芯片一览')
        out += '<div class="c-table c-table--links"><table><thead><tr><th>推荐芯片</th><th>对应产品</th><th>应用场景</th></tr></thead><tbody>'
        for (chip, route), titles in chips.items():
            slug = route.rsplit('/', 1)[-1] if route else ''
            prod = f'<a href="{route}">{E(pc(slug)["model"])} {E(pc(slug)["name"])}</a>' if slug in PRODUCTS else '—'
            out += f'<tr><td class="c-mono">{E(chip)}</td><td>{prod}</td><td>{E("、".join(titles))}</td></tr>'
        out += '</tbody></table></div>\n\n'
        out += section('其他应用领域')
        out += grid([app_card(x) for x in APPS if x['key'] != a['key']], 3)
        out += cta()
        write(f'applications/{a["key"]}.md', out)


# ---------- 磁仿真 ----------
def render_services():
    sc = page_copy('services')
    sv = S['services']
    out = fm(title=SEC['services'], description=sc.get('lead', ''), aside=False, pageClass='c-page')
    out += header([HOME, (SEC['services'], None)], SEC['services'],
                  sc.get('lead', '懂结构、懂设计、懂磁路、懂电路，陪客户把方案从可行性一路做到量产。'),
                  [dict(value=len(sv['strengths']), label='核心能力'), dict(value=len(sv['services']), label='服务环节'), dict(value=len(sv['cases']), label='仿真案例')],
                  kicker=BRAND)
    out += section('核心能力', '懂结构、懂设计、懂磁路、懂电路。')
    if sc.get('intro'):
        out += '\n\n'.join(sc['intro']) + '\n\n'
    out += '<div class="c-grid c-grid--3">' + ''.join(
        f'<div class="c-pillar"><span class="c-pillar__icon"><img src="{x["icon"]}" alt=""></span><h3>{E(x["title"])}</h3></div>' for x in sv['strengths']) + '</div>\n\n'
    out += section('解决思路', sc.get('approach', '通过磁学仿真、磁路设计，并与电路、结构低成本快速迭代，最终实现功能。'))
    out += '<div class="c-flow">' + ''.join(f'<span><em>{n}</em>{t}</span>' for n, t in enumerate(['磁路设计', '电路设计', '结构设计', '低成本快速迭代'], 1)) + '</div>\n\n'
    out += section('服务内容', '覆盖从立项评估到量产良率的四个环节。')
    out += '<div class="c-grid c-grid--2">'
    for n, x in enumerate(sv['services'], 1):
        out += (f'<div class="c-step"><span class="c-step__no">{n:02d}</span><h3>{E(x["title"])}</h3><ul>' +
                ''.join(f'<li>{E(pt)}</li>' for pt in x['points']) + '</ul></div>')
    out += '</div>\n\n'
    out += section('仿真案例')
    out += '<div class="c-grid c-grid--3">' + ''.join(
        f'<figure class="c-fig c-fig--card c-fig--fill"><img src="{IMG.get(f"svc/{n}", pth)}" alt="仿真案例 {n + 1}" loading="lazy"></figure>'
        for n, pth in enumerate(sv['cases'])) + '</div>\n\n'
    out += cta('让磁路设计少走弯路', '把结构图与需求发给我们，技术团队可协助完成可行性分析、选型与磁路仿真。')
    write('services.md', out)


# ---------- 技术洞见 ----------
def render_techtalks():
    tc = page_copy('techtalks')
    arts = S['techtalks']
    years = sorted({a['date'][:4] for a in arts}, reverse=True)
    out = fm(title=SEC['techtalks'], description=tc.get('lead', ''), aside=False, pageClass='c-page')
    out += header([HOME, (SEC['techtalks'], None)], SEC['techtalks'],
                  tc.get('lead', '围绕编码器精度、低延时、多对极校准与霍尔开关应用的技术文章。'),
                  [dict(value=len(arts), label='篇文章'), dict(value=f'{years[-1]}–{years[0]}', label='发布时间')], kicker=BRAND)
    for y in years:
        items = [(n, a) for n, a in enumerate(arts) if a['date'][:4] == y]
        out += section(f'{y} 年', f'共 {len(items)} 篇')
        out += grid([card(a['href'], IMG.get(f'tt/{n}', a['image']), a['title'], a['summary'], kicker=a['date'],
                          media_kind='photo', more='阅读全文', external=True) for n, a in items], 3)
    out += cta()
    write('tech-talks.md', out)


# ---------- 关于 ----------
def cert_title(q):
    m = re.search(r'ISO ?\d+', q)
    if m:
        return m.group(0)
    return ' / '.join(x for x in ('RoHS', 'REACH') if x in q) or '认证'


def render_about():
    ac = page_copy('about')
    ab = S['about']
    stats = COPY.get('home', {}).get('stats') or [dict(value='2016', label='成立年份'), dict(value='10余项', label='核心专利'),
                                                   dict(value='ISO 26262', label='功能安全体系认证'), dict(value='ISO 9001', label='质量管理体系认证')]
    out = fm(title=SEC['about'], description=ac.get('lead', ''), aside=False, pageClass='c-page')
    out += header([HOME, (SEC['about'], None)], SEC['about'], ac.get('lead', '智能感知世界，传递美好生活。'), stats, kicker=BRAND)
    out += section('公司简介')
    photos = [IMG[k] for k in sorted(IMG) if k.startswith('about/')]
    out += '<div class="c-split c-split--top"><div class="c-split__text">\n\n' + '\n\n'.join(ac.get('profile') or [ab['about'], ab['what']]) + '\n\n</div>'
    if photos:
        out += '<div class="c-split__media c-split__media--stack">' + ''.join(f'<img src="{p}" alt="公司环境" loading="lazy">' for p in photos) + '</div>'
    out += '</div>\n\n'
    out += section('核心价值观')
    out += '<div class="c-grid c-grid--3">' + ''.join(
        f'<div class="c-value"><span>{E(v["en"].upper())}</span><h3>{E(v["name"])}</h3><p>{E(v["desc"])}</p></div>' for v in ab['values']) + '</div>\n\n'
    out += section('核心优势')
    out += '\n\n'.join(ac.get('strength') or [ab['advantage']]) + '\n\n'
    out += section('品质认证')
    qs = ac.get('quality') or ab['quality']
    out += f'<div class="c-grid c-grid--{min(3, len(qs))}">' + ''.join(
        f'<div class="c-cert"><b>{E(cert_title(q))}</b><p>{E(q)}</p></div>' for q in qs) + '</div>\n\n'
    out += section('加入我们', '招聘邮箱 hr@conntek.com.cn，电话 0512-62982283。')
    out += '<div class="c-table c-jobs"><table><thead><tr><th>职位</th><th>人数</th><th>学历要求</th><th>工作地点</th><th>发布时间</th></tr></thead><tbody>'
    for j in ab['jobs']:
        out += f'<tr><td><b>{E(j["title"])}</b></td><td>{E(j["count"])}</td><td>{E(j["edu"])}</td><td class="c-nowrap">{E(j["city"])}</td><td class="c-nowrap">{E(j["date"])}</td></tr>'
    out += '</tbody></table></div>\n\n'
    for j in ab['jobs']:
        body, in_list = '', False
        for line in j['body']:
            line = re.sub(r'^(\d+)[\.、．]\s*', r'\1. ', line)
            is_item = bool(re.match(r'^\d+\. ', line))
            if re.match(r'^(工作内容具体描述|岗位职责|任职资格描述|任职要求)[:：]?$', line):
                body += f'\n\n**{line.rstrip("：:")}**\n\n'
                in_list = False
            elif is_item:
                body += line + '\n'
                in_list = True
            else:
                body += ('\n' if in_list else '') + line + '\n\n'
                in_list = False
        out += f'::: details {j["title"]} · {j["city"]} · {j["count"]} 人\n\n{body.strip()}\n\n:::\n\n'
    out += cta('期待与你同行', '投递简历或咨询职位，欢迎联系昆泰芯人力资源团队。',
               buttons=(('hr@conntek.com.cn', 'mailto:hr@conntek.com.cn'), ('0512-62982283', 'tel:0512-62982283'), (SEC['contact'], '/contact')))
    write('about/index.md', out)


# ---------- 联系 ----------
def render_contact():
    cc = page_copy('contact')
    ct = S['contact']
    out = fm(title=SEC['contact'], description=cc.get('lead', ''), aside=False, pageClass='c-page')
    out += header([HOME, (SEC['contact'], None)], SEC['contact'],
                  cc.get('lead', '总部位于泉州，在苏州、上海、南京、杭州设有研发中心，深圳设有运营中心。'),
                  [dict(value='泉州', label='总部'), dict(value='4 城', label='研发中心'), dict(value='深圳', label='运营中心')], kicker=BRAND)
    groups = [b for b in ct['blocks'] if not any('@' in i for i in b['items'])]
    channels = [b for b in ct['blocks'] if any('@' in i for i in b['items'])]
    out += section('业务联系', '销售、技术支持与招聘的直接联系方式。')
    out += '<div class="c-grid c-grid--3">'
    for b in channels:
        rows = ''.join(f'<a href="{"mailto:" if "@" in i else "tel:"}{i}">{E(i)}</a>' for i in b['items'])
        out += f'<div class="c-contact"><span>{E(b["en"].title())}</span><h3>{E(b["name"])}</h3>{rows}</div>'
    out += '</div>\n\n'
    out += section('公司地址')
    out += '<div class="c-grid c-grid--3">'
    for b in groups:
        rows = ''.join(f'<p>{E(i)}</p>' for i in b['items'])
        out += f'<div class="c-contact c-contact--addr"><span>{E(b["en"].title())}</span><h3>{E(b["name"])}</h3>{rows}</div>'
    out += '</div>\n\n'
    out += section('办公地点')
    out += grid([f'<figure class="c-city"><img src="{IMG.get(f"city/{n}", c["image"])}" alt="" loading="lazy"><figcaption><b>{E(c["name"])}</b><span>{E(c["en"].title())}</span></figcaption></figure>'
                 for n, c in enumerate(ct['cities'])], 4)
    out += cta('欢迎来访与合作', '预约拜访、样品申请或商务合作，请通过销售邮箱与我们联系。')
    write('contact.md', out)


# ---------- 首页 ----------
def render_home():
    hc = COPY.get('home', {})
    sec = hc.get('sections', {})
    stats = hc.get('stats') or [dict(value='2016', label='成立年份'), dict(value='10余项', label='核心专利'),
                                dict(value=len(PRODUCTS), label='产品系列'), dict(value='ISO 26262', label='功能安全体系认证')]
    out = f'''---
layout: home
title: 昆泰芯微电子
titleTemplate: CONNTEK
hero:
  name: {json.dumps(hc.get('title', BRAND), ensure_ascii=False)}
  text: {json.dumps(hc.get('slogan', '智能感知世界 传递美好生活'), ensure_ascii=False)}
  tagline: {json.dumps(hc.get('tagline', '专注于面向物联网应用的传感器芯片研发、生产与销售'), ensure_ascii=False)}
  image:
    src: /img/ref/hero-magnet-sensor-render.webp
    alt: 磁铁与磁传感器芯片
  actions:
    - theme: brand
      text: 浏览产品
      link: /products/
    - theme: alt
      text: {SEC['applications']}
      link: /applications/
    - theme: alt
      text: {SEC['contact']}
      link: /contact
---

<div class="c-home">

'''
    out += stat_row(stats)

    def hsec(key, title, lead, link, link_text):
        s = sec.get(key, {})
        return (f'<div class="c-home__head"><div><h2>{E(title)}</h2><p>{E(s.get("lead", lead))}</p></div>'
                f'<a class="c-link" href="{link}">{E(link_text)}</a></div>\n\n')

    out += hsec('products', SEC['products'], '从三轴霍尔到 30 bit 细分器，覆盖磁传感的主要品类。', '/products/', '全部产品')
    out += grid([category_card(c) for c in CATS], 5)
    featured = ['kth78', 'ktm52', 'ktm58', 'ktm59', 'kth71', 'kth57', 'ktm13', 'kth25']
    out += hsec('featured', '主推产品', '高精度磁编码器与高可靠磁开关。', '/products/encoder/', '编码器芯片')
    out += grid([product_card(s) for s in featured if s in PRODUCTS], 4)
    out += hsec('applications', SEC['applications'], '消费电子、智能生活、工业 4.0 与智能交通。', '/applications/', '全部应用')
    out += grid([app_card(a) for a in APPS], 4)
    sv = S['services']
    out += hsec('services', SEC['services'], '懂结构、懂设计、懂磁路、懂电路。', '/services', '了解服务')
    out += '<div class="c-grid c-grid--4">' + ''.join(
        f'<a class="c-step c-step--link" href="/services"><span class="c-step__no">{n:02d}</span><h3>{E(x["title"])}</h3><ul>'
        + ''.join(f'<li>{E(pt)}</li>' for pt in x['points']) + '</ul></a>'
        for n, x in enumerate(sv['services'], 1)) + '</div>\n\n'
    v = S['home']['video']
    out += hsec('about', SEC['about'], '智能感知世界，传递美好生活。', '/about/', '公司介绍')
    ab = COPY.get('pages', {}).get('about', {}).get('profile') or [S['about']['about']]
    out += (f'<div class="c-split"><div class="c-split__media c-split__media--video"><video controls preload="none" poster="{IMG.get("poster/home", v["poster"])}" src="{v["src"]}"></video></div>'
            f'<div class="c-split__text">\n\n{ab[0]}\n\n<div class="c-tags"><span>ISO 26262</span><span>ISO 9001</span><span>RoHS</span><span>REACH</span></div>\n\n</div></div>\n\n')
    out += hsec('techtalks', SEC['techtalks'], '编码器精度、低延时与多对极校准的技术文章。', '/tech-talks', '全部文章')
    out += grid([card(a['href'], IMG.get(f'tt/{n}', a['image']), a['title'], a['summary'], kicker=a['date'], media_kind='photo', more='阅读全文', external=True)
                 for n, a in enumerate(S['techtalks'][:3])], 3)
    out += cta()
    out += '\n</div>\n'
    write('index.md', out)


# ---------- 导航与侧边栏 ----------
def render_nav():
    prod_items = [{'text': f"{SEC['products']}总览", 'link': '/products/'}]
    side_products = [{'text': f"{SEC['products']}总览", 'link': '/products/'}]
    for c in CATS:
        slugs = [i['slug'] for i in c['items']] + [s for s, p in PRODUCTS.items() if p['category'] == c['key'] and s not in ITEM_BY_SLUG]
        prod_items.append({'text': c['name'], 'items': [{'text': f'{pc(s)["model"]} · {pc(s)["name"]}', 'link': PRODUCTS[s]['route']} for s in slugs]})
        side_products.append({'text': c['name'], 'collapsed': False, 'items': [{'text': f'{c["name"]}总览', 'link': f'/products/{c["key"]}/'}] +
                              [{'text': f'{pc(s)["model"]} {pc(s)["name"]}', 'link': PRODUCTS[s]['route']} for s in slugs]})
    apps = [{'text': f"{SEC['applications']}总览", 'link': '/applications/'}] + [{'text': a['name'], 'link': f'/applications/{a["key"]}'} for a in APPS]
    nav = [
        {'text': SEC['products'], 'activeMatch': '^/products/', 'items': prod_items},
        {'text': SEC['applications'], 'activeMatch': '^/applications/', 'items': apps},
        {'text': '服务与洞见', 'activeMatch': '^/(services|tech-talks)', 'items': [
            {'text': SEC['services'], 'link': '/services'}, {'text': SEC['techtalks'], 'link': '/tech-talks'}]},
        {'text': SEC['about'], 'activeMatch': '^/(about|contact)', 'items': [
            {'text': '公司简介', 'link': '/about/#公司简介'}, {'text': '核心价值观', 'link': '/about/#核心价值观'},
            {'text': '品质认证', 'link': '/about/#品质认证'}, {'text': '加入我们', 'link': '/about/#加入我们'},
            {'text': SEC['contact'], 'link': '/contact'}]},
    ]
    json.dump({'nav': nav, 'products': side_products, 'applications': apps},
              open(os.path.join(DOCS, '.vitepress', 'sidebar.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main():
    for slug in ORDER:
        render_product(slug)
    render_products()
    render_applications()
    render_services()
    render_techtalks()
    render_about()
    render_contact()
    render_home()
    render_nav()
    print('rendered', len(PRODUCTS), 'products + index pages')


if __name__ == '__main__':
    main()
