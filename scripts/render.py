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
APP_TAGS = load('content/app_tags.json', {})
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


WRITTEN = set()


def write(rel, content):
    fn = os.path.join(DOCS, rel)
    WRITTEN.add(os.path.normcase(os.path.abspath(fn)))
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
# 原站图太小的，换成从产品手册里取的清晰版
FIG_OVERRIDE = {'/images/Absolute-angle-divider-.png': '/images/ktm5800-magnet-placement.png'}


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


def fig_table(f, note=''):
    """图片转写出来的表，走与规格表完全相同的一套表现方式（同一个 spec_entry）。"""
    tb = f['table']
    head = tb.get('header') or []
    t = dict(title=tb.get('title') or f.get('caption') or '', layout='matrix',
             columns=[str(c) for c in (head[-1] if head else [])],
             rows=[[str(c) for c in r] for r in tb.get('rows') or []],
             merge_cols=[0, 1] if tb.get('merge') else [],
             notes=([note] if note else []))
    if not t['columns'] and t['rows']:
        t['columns'] = [''] * len(t['rows'][0])
    t['merge_cols'] = [c for c in t['merge_cols'] if c < len(t['columns'])]
    return spec_entry(t)


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


MAX_COMPARE = 5     # 一张对比表最多放几个型号，保证不横向滚动


def transposed_table(cols, rows, merge, skip=(), link=False, prod=None):
    """参数竖排、型号横排：同一张表里可以逐行比较各型号。"""
    idc = id_index(cols)
    skip = set(skip) | {idc}
    heads = [r[idc] for r in rows]
    def head_cell(h):
        inner = cell_html(h)
        if link and prod:
            inner = f'<a href="{model_link(prod, h)}">{inner}</a>'
        return f'<th scope="col" class="c-mono">{inner}</th>'
    out = '<div class="c-table c-table--t" tabindex="0" role="region" aria-label="参数对比表"><table><thead><tr><th>参数</th>' + ''.join(head_cell(h) for h in heads) + '</tr></thead><tbody>'
    body = ''
    for ci, name in enumerate(cols):
        if ci in skip:
            continue
        vals = [r[ci] if ci < len(r) else '—' for r in rows]
        if all(is_empty(v) for v in vals):
            continue
        if all(v == vals[0] for v in vals) and len(vals) > 1:
            body += f'<tr><th scope="row">{E(name)}</th><td colspan="{len(vals)}">{cell_html(vals[0])}</td></tr>'
        else:
            body += f'<tr><th scope="row">{E(name)}</th>' + ''.join(f'<td>{cell_html(v)}</td>' for v in vals) + '</tr>'
    return out + body + '</tbody></table></div>\n\n' if body else ''


def compare_tables(cols, rows, merge, group_by=None, link=False, prod=None):
    """型号多时：按分组（等级/系列）拆成若干张对比表，每张最多 MAX_COMPARE 个型号。"""
    groups = OrderedDict()
    for r in rows:
        g = str(r[group_by]).strip() if isinstance(group_by, int) and group_by < len(r) else ''
        groups.setdefault(g, []).append(r)
    skip = [group_by] if isinstance(group_by, int) else []
    out = ''
    for g, grows in groups.items():
        chunks = [grows[i:i + MAX_COMPARE] for i in range(0, len(grows), MAX_COMPARE)]
        for n, chunk in enumerate(chunks, 1):
            label = g + (f'（{n}/{len(chunks)}）' if len(chunks) > 1 else '')
            if label:
                out += f'<p class="c-table-sub">{E(label)}</p>\n\n'
            out += transposed_table(cols, chunk, merge, skip, link=link, prod=prod)
    return out


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


def spec_entry(t):
    """content/specs.json 的一张表：matrix 为型号矩阵，keyvalue 为参数两两成对的四列表。"""
    out = f'<p class="c-table-title">{E(t["title"])}</p>\n\n' if t.get('title') and t['title'] != '规格参数' else ''
    if t.get('layout') == 'keyvalue':
        items = t.get('items') or []
        out += '<div class="c-table c-kv"><table><tbody>'
        for i in range(0, len(items), 2):
            out += '<tr>'
            for k, v in items[i:i + 2]:
                out += f'<th scope="row">{E(k)}</th><td>{cell_html(v)}</td>'
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
                return out + transposed_table(cols, rows, merge) + notes_html(t)
            return out + model_cards(cols, rows, merge) + notes_html(t)
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


MODEL_RE = re.compile(r'(KT[A-Z]\d{3,4})', re.I)


def base_model(v):
    m = MODEL_RE.search(str(v))
    return m.group(1).upper() if m else str(v).strip()


def as_matrix(t):
    """统一成 (title, columns, rows, merge_cols)；keyvalue 表返回 None。"""
    if t.get('layout') == 'keyvalue' or not t.get('columns'):
        return None
    return t


def merged_spec(slug, spec_tables, fig_tables):
    """产品页用：把合并后的型号矩阵渲染成分组对比表。"""
    m = merged_matrix(slug, spec_tables, fig_tables)
    if not m:
        return None, []
    return compare_tables(m['cols'], m['rows'], [], m['grade'], link=True, prod=slug), m['conflicts']


def merged_matrix(slug, spec_tables, fig_tables):
    """把同一产品的全部型号表（HTML 表 + 图片转写表）合并成一张矩阵。

    - 字段按首次出现顺序合并，来源不同但同值的只显示一次
    - 同一字段两份来源不一致时并列显示并在下方列出差异，不丢信息
    - 完整型号（带封装后缀）作为该型号下的「订购型号」明细保留
    返回 dict(cols, rows, grade, conflicts)；没有型号表时返回 None
    """
    syn = {'支持': '是', '有': '是', '不支持': '否', '无': '否', '选配': '可选'}
    # 两处来源对同一参数的不同叫法，归到同一个字段，避免卡片里出现两行同义参数
    label_syn = {'供电': '供电电压', '电压': '供电电压', '接口': '输出接口', '输出方式': '输出接口',
                 '温度范围': '工作温度', '角度刷新速率': '角度刷新频率', '噪声': '噪声（1σ）',
                 'crc校验': 'CRC 校验', 'abz分辨率': 'ABZ 分辨率', 'pwm频率': 'PWM 频率',
                 '系统延时': '系统延时（匀速）', '磁场检测范围': '工作磁场'}

    def label_key(name):
        k = re.sub(r'[\s]', '', str(name)).lower()
        k = re.sub(r'[（(][^）)]*[）)]', '', k)
        return label_syn.get(k, name)

    def norm(v):
        """比较用的归一化：写法/单位/顺序差异不算差异，只留真正取值不同的。"""
        x = str(v).lower().replace('≈', '').replace('约', '')
        x = re.sub(r'[（(][^）)]*[）)]', '', x)
        x = re.sub(r'[\s,，]', '', x)
        x = x.replace('℃', '').replace('°c', '').replace('－', '-').replace('～', '~').replace('至', '~').replace('／', '/')
        x = syn.get(x, x)
        toks = sorted(syn.get(t, t) for t in re.split(r'[/、]', x) if t)
        return '|'.join(toks), tuple(re.findall(r'-?\d+(?:\.\d+)?', x))

    mats = []
    for t in spec_tables:
        m = as_matrix(t)
        if m:
            mats.append((t.get('title') or '规格参数', m))
    for f in fig_tables:
        tb = f.get('table') or {}
        head = tb.get('header') or []
        if not tb.get('rows'):
            continue
        cols = [str(c) for c in (head[-1] if head else [])]
        if len(cols) < 3:      # 参数/数值 这类整体参数表不参与合并
            continue
        mats.append((tb.get('title') or f.get('caption') or '补充参数',
                     dict(columns=cols, rows=[[str(c) for c in r] for r in tb['rows']],
                          merge_cols=[0, 1] if tb.get('merge') else [])))
    if not mats:
        return None

    # 以信息量最大的一张表为准：它的每一行（每个订购型号）都保留；
    # 其余来源按型号前缀补它没有的字段，取值不同的只列差异，不覆盖
    mats.sort(key=lambda m: len(m[1]["rows"]) * len(m[1]["columns"]), reverse=True)
    badge_names = ("等级", "类型")
    title, t = mats[0]
    cols, rows = t["columns"], t["rows"]
    idc = id_index(cols)
    fields, grade_name = [], next((c for c in cols if c in badge_names), None)
    for c in cols:
        lk = label_key(c)
        if c != cols[idc] and c != grade_name and lk not in fields:
            fields.append(lk)
    recs = []
    for row in rows:
        rec = {}
        for ci, name in enumerate(cols):
            v = str(row[ci]).strip()
            if ci == idc or name == grade_name or v in ("", "—"):
                continue
            rec.setdefault(label_key(name), v)
        recs.append(dict(id=str(row[idc]).strip(), base=base_model(row[idc]),
                         grade=str(row[cols.index(grade_name)]).strip() if grade_name else "", f=rec))

    conflicts, seen = [], set()
    for ti, (title2, t2) in enumerate(mats[1:], 1):
        c2, r2 = t2["columns"], t2["rows"]
        id2 = id_index(c2)
        for row in r2:
            base = base_model(row[id2])
            targets = [r for r in recs if r["base"] == base]
            if not targets:
                continue
            for ci, name in enumerate(c2):
                v = str(row[ci]).strip()
                if ci == id2 or is_empty(v) or name in badge_names:
                    continue
                lk = label_key(name)
                if lk not in fields:
                    fields.append(lk)
                same_field = [r["f"].get(lk) for r in targets if r["f"].get(lk)]
                if not same_field:
                    for r in targets:
                        r["f"][lk] = v
                elif all(norm(x) != norm(v) for x in same_field) and (base, lk) not in seen:
                    seen.add((base, lk))
                    conflicts.append(f'{base}「{lk}」：{same_field[0]} 或 {v}')

    head_cols = ["型号"] + ([grade_name] if grade_name else []) + fields
    out_rows = [[r["id"]] + ([r["grade"]] if grade_name else []) + [r["f"].get(n, "—") for n in fields] for r in recs]
    gi = 1 if grade_name and len({r[1] for r in out_rows}) > 1 else None
    return dict(cols=head_cols, rows=out_rows, grade=gi, conflicts=conflicts)


def series_tables(spec_tables, fig_tables):
    """整体参数表（参数/数值两列）单独保留，作为系列通用参数。"""
    out = ''
    for t in spec_tables:
        if t.get('layout') == 'keyvalue':
            out += spec_entry(t)
    for f in fig_tables:
        tb = f.get('table') or {}
        head = tb.get('header') or []
        cols = [str(c) for c in (head[-1] if head else [])]
        if tb.get('rows') and len(cols) < 3:
            out += fig_table(f)
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
            tables.append(f)
        else:
            diagrams.append((FIG_OVERRIDE.get(pth, pth), (f or {}).get('caption', '')))
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


def c_sel(slug):
    return pc(slug)['selection_note']


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
        body += app_tag_rows(c['applications'])
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
                f'<a href="{i}" target="_blank"><img src="{i}" alt="{E(c["model"])}产品形态图" loading="lazy"></a>' for i in imgs) + '</div>\n\n'

    tables, diagrams = figures_for(slug, p['figures'])
    specs = SPECS.get(slug) or []
    for t in specs:
        diagrams += [(FIG_OVERRIDE.get(f['src'], f['src']), f.get('caption', '')) for f in t.get('figures', [])
                     if FIG_OVERRIDE.get(f['src'], f['src']) not in [d for d, _ in diagrams]]
    spec_html = series_tables(specs, tables)
    cards, conflicts = merged_spec(slug, specs, tables)
    if cards:
        spec_html += cards
        if conflicts:
            spec_html += ('<details class="c-more"><summary>以下 '
                          + f'{len(conflicts)} 项参数存在两种标注，选型前请以产品手册为准</summary>\n\n<ul>'
                          + ''.join('<li>' + E(x) + '</li>' for x in conflicts) + '</ul>\n\n</details>\n\n')
    elif not specs:
        for sp in p['specs']:
            if re.sub(r'<[^>]+>', '', sp).strip():
                spec_html += clean_spec(sp)
    if diagrams:
        spec_html += '<div class="c-figs">' + ''.join(
            f'<figure class="c-fig"><img src="{d}" alt="{E(cap)}" loading="lazy">' + (f'<figcaption>{E(cap)}</figcaption>' if cap else '') + '</figure>'
            for d, cap in diagrams) + '</div>\n\n'
    if spec_html.strip():
        out += section('规格参数', c_sel(slug)) + spec_html

    if p['docs']:
        out += section('技术文档', '产品手册、评估套件说明与上位机软件，点击文件名直接下载。')
        out += docs_table(p['docs'])
    if p['videos']:
        out += section('视频资料')
        out += video_grid(slug, p['videos'])

    rel = related_cases(p['route'])
    if rel:
        out += section('应用案例', f'以下场景推荐使用 {c["model"]}。')
        out += grid([card(case_link(a, cse), IMG.get(f'case/{a["key"]}/{n}'), cse['title'], kicker=a['name'], media_kind='case')
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


MODEL_INDEX = {}


def series_prefix(model_text):
    m = re.search(r'(KT[A-Z]\d{2})', str(model_text).upper())
    return m.group(1) if m else ''


def _family_map():
    out = {}
    for sl in PRODUCTS:
        pre = series_prefix(pc(sl)['model'])
        if pre:
            out.setdefault(pre, sl)
    return out


FAMILY_OWNER = None


def owner_of(mid):
    """这个型号属于哪个产品页；映射不到就返回空。"""
    global FAMILY_OWNER
    if FAMILY_OWNER is None:
        FAMILY_OWNER = _family_map()
    pre = series_prefix(mid)
    return FAMILY_OWNER.get(pre, '')


def model_link(slug, mid):
    """本系列的型号进型号页；表里混进来的别系列型号，链到它自己的系列页。"""
    own = owner_of(mid)
    if own and own != slug and series_prefix(pc(slug)['model']):
        return PRODUCTS[own]['route']
    return model_route(slug, mid)
EMPTY_VALS = ('', '-', '—', '/', '／', 'n/a', 'na')


def is_empty(v):
    return str(v).strip().lower() in EMPTY_VALS


def split_models(mid):
    """一格里塞了多个型号（换行或 / 分隔）时拆开。"""
    parts = [x.strip() for x in re.split(r'[\n、,，]|\s/\s', str(mid)) if x.strip()]
    return parts or [str(mid).strip()]


def value_for(v, mid):
    """取值里按后缀分档写法（A1: 1.5 mV / A2: 2.0 mV）时，挑出该型号那一档。"""
    text = str(v)
    if ':' not in text and '：' not in text:
        return text
    suffix = re.sub(r'^.*?([A-Z]\d)$', r'\1', mid.strip())
    lines = [x.strip() for x in re.split(r'[\n]', text) if x.strip()]
    if len(lines) <= 1:
        lines = [x.strip() for x in re.split(r'(?<=[A-Za-z0-9])\s{2,}', text) if x.strip()]
    for line in lines:
        head = re.split(r'[:：]', line, 1)[0].strip()
        if head and (head == suffix or mid.endswith(head)):
            return re.split(r'[:：]', line, 1)[1].strip()
    return text


# ---------- 型号详情页 ----------
CHIP_PRIORITY = ['分辨率', '精度', '角度 INL', '非线性误差', '转速', '供电电压', '功耗', '平均功耗',
                 '工作频率', '灵敏度', '噪声（1σ）', '噪声', '输出接口', '工作温度', '封装']


def clean_mid(mid):
    """型号单元格里可能有换行或多个型号，压成一行。"""
    return re.sub(r'\s*[\n/、]\s*', ' / ', str(mid).strip())


def model_slug(mid):
    return re.sub(r'[^a-z0-9]+', '-', str(mid).lower()).strip('-')


def model_route(prod_slug, mid):
    return f"{PRODUCTS[prod_slug]['route']}/{model_slug(mid)}"


def doc_matches(series, mid):
    """技术文档的「产品系列」与型号是否对应：KTH78XX / KTH7801 / KTH462N系列 都能匹配上。"""
    a = re.sub(r'[^A-Z0-9]', '', str(series).upper()).rstrip('X')
    b = re.sub(r'[^A-Z0-9]', '', str(mid).upper())
    return bool(a) and (b.startswith(a) or a.startswith(b[:7]))


def model_chips(fields):
    out = []
    for name in CHIP_PRIORITY:
        v = fields.get(name)
        if v and v != '—' and not any(c['label'] == name for c in out):
            out.append(dict(label=name, value=v))
        if len(out) == 4:
            break
    return out


SPEC_ORDER = ('分辨率', '精度', '角度 INL', '非线性误差', '噪声（1σ）', '噪声', '转速', '供电电压',
              '功耗', '平均功耗', '工作频率', '灵敏度', '输出接口', '封装', '工作温度')
DIFF_ORDER = ('封装', '输出接口', 'CRC 校验', '分辨率', '噪声（1σ）', '精度', '灵敏度', '工作频率',
              '平均功耗', '功耗', 'BOP', '工作温度', '类型')


def _phrase(name, value):
    if name == '封装':
        return f'{value} 封装'
    if name in ('输出接口', '输出方式'):
        return str(value) if '输出' in str(value) else f'{value} 输出'
    if name == 'CRC 校验':
        return ('带 CRC 校验' if value in ('是', '可选') else '不带 CRC 校验')
    return f'{value} {name}'


GRADES = ('车规', '工业', '消费')
UNIT_SCALE = {'n': 1e-9, 'μ': 1e-6, 'u': 1e-6, 'm': 1e-3, '': 1, 'k': 1e3, 'K': 1e3, 'M': 1e6, 'G': 1e9}
# 字段 -> (越小越好?, 这一项强在哪的说法)
SUPERLATIVE = {
    '噪声（1σ）': (True, '本系列噪声最低'),
    '噪声': (True, '本系列噪声最低'),
    '角度 INL': (True, '本系列非线性误差最小'),
    '非线性误差': (True, '本系列非线性误差最小'),
    '平均功耗': (True, '本系列功耗最低'),
    '功耗': (True, '本系列功耗最低'),
    '转速': (False, '本系列支持转速最高'),
    '工作频率': (False, '本系列工作频率最高'),
    '分辨率': (False, '本系列分辨率最高'),
    '灵敏度': (False, '本系列灵敏度最高'),
}


def num_of(v):
    """取值里的第一个数字，按 n / μ / m / k / M 前缀折算，取不到返回 None。"""
    m = re.search(r'(-?\d+(?:\.\d+)?)\s*([nμumkKMG]?)', str(v).replace(',', ''))
    if not m:
        return None
    try:
        return float(m.group(1)) * UNIT_SCALE.get(m.group(2), 1)
    except ValueError:
        return None


def superlative_of(mid, fields_of, order):
    """本型号在同系列里是否有某项最优；只在该项确实有差异时才给。"""
    for name, (lower_better, text) in SUPERLATIVE.items():
        vals = {m: num_of(f.get(name)) for m, f in fields_of.items() if f.get(name)}
        vals = {m: v for m, v in vals.items() if v is not None}
        if len(vals) < 2 or len(set(vals.values())) < 2 or mid not in vals:
            continue
        best = min(vals.values()) if lower_better else max(vals.values())
        if vals[mid] == best and list(vals.values()).count(best) == 1:
            return text
    return ''



def model_summary(series_model, series_name, grade, fields, diff_pairs, use_text='', edge='', use_differs=False):
    """一段 ~100 字的型号说明：定位 → 本型号区别于同系列的取值 → 共有关键指标 → 典型用途。"""
    diff_names = [n for n, _ in diff_pairs]
    diffs = [_phrase(n, v) for n, v in diff_pairs]
    specs = []
    for n in SPEC_ORDER:
        v = fields.get(n)
        if v and not is_empty(v) and n not in diff_names and len(specs) < (1 if len(diffs) >= 3 else (2 if diffs else 4)):
            specs.append(_phrase(n, v))
    base = f'{series_model} {series_name}' if re.match(r'^[A-Za-z0-9]', str(series_name)) else f'{series_model}{series_name}'
    if grade in GRADES:
        role = f'{base}的{grade}级型号'
    elif grade and not is_empty(grade):
        role = f'{base}中的{grade}型号'
    else:
        role = f'{base}的型号之一'
    out = role + ('，' + '、'.join(diffs) if diffs else '') + ('；' + '、'.join(specs) if specs else '') + '。'
    if edge:
        out += f'{edge}。'
    if use_text:
        out += ('该等级面向' if use_differs else '典型用于') + use_text + '。'
    return out


DIFF_FIELDS = ('封装', '输出接口', '分辨率', '精度', '角度 INL', '噪声（1σ）', '供电电压', '平均功耗',
               '功耗', '工作频率', 'BOP', '灵敏度', '工作温度', '转速')


def model_lead(series_name, grade, fields, mid=''):
    bits = []
    if grade:
        bits.append(f'{grade}级')
    for n in DIFF_FIELDS:
        v = fields.get(n)
        if v and v != '—':
            bits.append(f'{v} {n}' if n not in ('封装',) else f'{v} 封装')
        if len(bits) >= 4:
            break
    head = f'{mid}：' if mid else ''
    return head + (series_name + ('，' if series_name and bits else '')) + '、'.join(bits)


def render_model_pages(slug, matrix):
    """把合并后的型号矩阵拆成一张张型号详情页，格式全站统一。"""
    p, c = PRODUCTS[slug], pc(slug)
    cat = CAT_BY_KEY[p['category']]
    cols, rows, gi = matrix['cols'], matrix['rows'], matrix['grade']
    field_names = [n for i, n in enumerate(cols) if i != 0 and i != gi]
    pages = []
    conflicts_by_model = {}
    for c_txt in matrix.get('conflicts') or []:
        key = re.split(r'[「]', c_txt)[0].strip()
        conflicts_by_model.setdefault(key, []).append(c_txt)
    expanded = []
    own_prefix = series_prefix(c['model'])
    for row in rows:
        for one in split_models(row[0]):
            other_owner = owner_of(one)
            if own_prefix and other_owner and other_owner != slug:
                continue      # 该型号属于别的系列页，这里不重复出页面
            expanded.append((one, row))
    if not expanded:
        return []
    fields_of, grade_of = {}, {}
    for one, orow in expanded:
        f = {cols[i]: value_for(v, one) for i, v in enumerate(orow) if i not in (0, gi) and not is_empty(v)}
        fields_of[one] = {k: v for k, v in f.items() if not is_empty(v)}
        grade_of[one] = str(orow[gi]).strip() if gi is not None else ''
    # 每个字段在本系列里是否存在差异
    varying = [n for n in cols[1:] if len({fields_of[m].get(n, '') for m, _ in expanded}) > 1]
    diff_of = {}
    for one, _ in expanded:
        ordered = [n for n in DIFF_ORDER if n in varying] + [n for n in varying if n not in DIFF_ORDER]
        diff_of[one] = [(n, fields_of[one][n]) for n in ordered if fields_of[one].get(n)]
    # 摘要重复时逐步多带一个差异项，直到本系列内唯一
    summary_of, use_of = {}, {}
    for one, _ in expanded:
        f = fields_of[one]
        use_txt = f.get('应用领域') or '、'.join((c.get('applications') or [])[:4])
        use_txt = re.sub(r'\s+', ' ', str(use_txt)).strip()
        if len(use_txt) > 26:
            cut = use_txt[:26]
            sep = max(cut.rfind('、'), cut.rfind('，'), cut.rfind(','), cut.rfind(' '))
            use_txt = (cut[:sep] if sep > 8 else cut).rstrip('、，, ') + '等'
        use_of[one] = use_txt
    use_differs = len({use_of[one] for one, _ in expanded}) > 1
    edge_of = {one: superlative_of(one, fields_of, cols) for one, _ in expanded}
    for k in range(3, 7):
        summary_of = {one: model_summary(c['model'], c['name'], grade_of[one], fields_of[one],
                                         diff_of[one][:k], use_of[one], edge_of[one], use_differs)
                      for one, _ in expanded}
        if len(set(summary_of.values())) == len(summary_of):
            break
    for mid, row in expanded:
        grade = grade_of[mid]
        fields = fields_of[mid]
        docs = [d for d in p['docs'] if doc_matches(d['series'], mid)]
        route = model_route(slug, mid)
        lead_txt = summary_of[mid]
        out = fm(title=f'{mid} · {c["model"]}{c["name"]}', description=lead_txt,
                 aside=False, pageClass='c-page c-page--model')
        out += eyebrow(HOME, (SEC['products'], '/products/'), (cat['name'], f'/products/{cat["key"]}/'),
                       (c['model'], p['route']), (mid, None))
        out += f'<p class="c-kicker">{E(c["model"])} {E(c["name"])}</p>\n\n# {mid}\n\n'
        out += f'<p class="c-lead">{E(lead_txt)}</p>\n\n'
        out += chips_block(model_chips(fields))
        out += '<div class="c-actions">'
        out += (f'<a class="c-btn c-btn--brand" href="#技术文档">下载技术文档<small>{sum(1 for d in docs for k in ("cn", "en") if d[k])}</small></a>'
                if docs else '<a class="c-btn c-btn--brand" href="/contact">索取产品资料</a>')
        out += f'<a class="c-btn" href="/contact">申请样品 / 咨询</a><a class="c-btn" href="{p["route"]}">查看 {E(c["model"])}</a></div>\n\n'

        out += section('参数详情', f'{mid} 的全部参数，取自{c["model"]}规格表。')
        items = [(n, fields[n]) for n in field_names if fields.get(n)]
        out += '<div class="c-table c-kv"><table><tbody>'
        for i in range(0, len(items), 2):
            out += '<tr>'
            for n, v in items[i:i + 2]:
                out += f'<th>{E(n)}</th><td>{cell_html(v)}</td>'
            if len(items[i:i + 2]) == 1:
                out += '<th></th><td></td>'
            out += '</tr>'
        out += '</tbody></table></div>\n\n'

        mine = conflicts_by_model.get(base_model(mid), [])
        if mine:
            out += ('<p class="c-note">以下参数在资料中有两种标注，选型前请以产品手册为准：'
                    + E('；'.join(x.split('「', 1)[-1].replace('」', ' ') for x in mine)) + '</p>\n\n')
        peers = [r for r in rows if (gi is None or r[gi] == row[gi])]
        if len(peers) > 1:
            same = [r for r in peers if r[0] != row[0]][:MAX_COMPARE - 1]
            out += section('同系列对比', f'与{grade + "级" if grade else c["model"]}其他型号的差异。')
            out += transposed_table(cols, [row] + same, [], [gi] if gi is not None else [])
        if docs:
            out += section('技术文档', '产品手册与相关资料，点击文件名直接下载。')
            out += docs_table(docs)
        out += section('所属产品系列', f'{c["model"]}共 {len(expanded)} 个型号，点方块直接跳转。')
        out += '<div class="c-series-box">'
        out += card(p['route'], product_visual(slug), c['name'], c['lead'], kicker=c['model'],
                    media_kind='icon' if icon(slug) else 'product', more='查看系列')
        # 所有方块用同一组字段、同一顺序，纵向对齐好读
        tile_fields = [n for n, _ in diff_of[mid]][:2]
        for other, _ in expanded:
            for n, _v in diff_of[other]:
                if len(tile_fields) >= 2:
                    break
                if n not in tile_fields:
                    tile_fields.append(n)
        for n in ('CRC 校验', 'CRC校验'):
            if n in varying and n not in tile_fields:
                tile_fields.append(n)
        if not tile_fields:
            tile_fields = [n for n in ('封装', '输出接口') if any(fields_of[o].get(n) for o, _ in expanded)][:2]
        tiles = ''
        grade_label = cols[gi] if gi is not None else ''
        for other, _ in expanded:
            cur = ' c-tile--cur' if other == mid else ''
            rows_html = ''
            if grade_label and grade_of[other]:
                rows_html += f'<span class="c-tile__grade">{E(grade_of[other])}</span>'
            for n in tile_fields:
                v = fields_of[other].get(n, '')
                if is_empty(v):
                    continue
                short = n.replace(' 校验', '').replace('输出接口', '').replace('封装', '').strip()
                if str(v) in ('是', '可选', '有'):
                    txt = f'有 {short}' if short else str(v)
                elif str(v) in ('否', '无', '不支持'):
                    txt = f'无 {short}' if short else str(v)
                else:
                    txt = str(v)
                rows_html += f'<span>{E(txt)}</span>'
            tiles += (f'<a class="c-tile{cur}" href="{model_route(slug, other)}"><b>{E(other)}</b>'
                      + rows_html + '</a>')
        out += f'<div class="c-tiles">{tiles}</div></div>\n\n'
        out += cta()
        write(route.lstrip('/') + '.md', out)
        pages.append((mid, route, grade))
    MODEL_INDEX[slug] = pages
    return pages


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
        cg = CAT_GUIDES.get(c['key'], {})
        if cg.get('intro'):
            out += '\n\n'.join(cg['intro']) + '\n\n'
        if cg.get('how_to_choose'):
            out += section('怎么选', '按下面几步缩小范围。')
            out += '<div class="c-features">' + ''.join(
                '<div class="c-feature"><span class="c-feature__no">%02d</span><div><h3>%s</h3><p>%s</p></div></div>' % (i, E(x['step']), E(x['desc']))
                for i, x in enumerate(cg['how_to_choose'], 1)) + '</div>\n\n'
        if cg.get('compare', {}).get('rows'):
            out += section('系列对照')
            cmp = cg['compare']
            out += '<div class="c-table c-table--links"><table><thead><tr>' + ''.join('<th>%s</th>' % E(x) for x in cmp['columns']) + '</tr></thead><tbody>'
            for row in cmp['rows']:
                cells = []
                for ci, v in enumerate(row):
                    if ci == 0:
                        sl = next((x for x in PRODUCTS if pc(x)['model'] == v), '')
                        cells.append('<td>%s</td>' % (('<a href="%s">%s</a>' % (PRODUCTS[sl]['route'], E(v))) if sl else E(v)))
                    else:
                        cells.append('<td>%s</td>' % cell_html(v))
                out += '<tr>' + ''.join(cells) + '</tr>'
            out += '</tbody></table></div>\n\n'
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
                cards.append(card(case_link(a, cse), IMG.get(f'case/{a["key"]}/{n}'), cse['title'], kicker=cse['chip'], media_kind='case'))
            out += grid(cards[:8], 4)
        if cg.get('faq'):
            out += section('常见问题')
            for q in cg['faq']:
                out += '::: details %s\n\n%s\n\n:::\n\n' % (q['q'], q['a'])
        out += section('其他产品线')
        out += grid([category_card(x) for x in CATS if x['key'] != c['key']], 4)
        out += cta()
        write(f'products/{c["key"]}/index.md', out)


# ---------- 应用案例详情页 ----------
CASES = load('content/cases.json', {})
APP_GUIDES = load('content/app_guides.json', {})
CAT_GUIDES = load('content/category_guides.json', {})
GLOSSARY = load('content/glossary.json', {})


def case_entry(area_key, title):
    """按标题找到案例文案，返回 (slug, data)；没有就返回 (None, None)。"""
    for slug, d in (CASES.get(area_key) or {}).items():
        if slug.startswith('_'):
            continue
        if d.get('title') == title:
            return slug, d
    return None, None


def case_page_route(area_key, title):
    slug, _ = case_entry(area_key, title)
    return f'/applications/{area_key}/{slug}' if slug else None


def normalize_app_tags(tags):
    """把产品页的应用标签过一遍受控词表：先拆、再归并、再按坐标轴分组。

    见 content/app_tags.json 的 _doc。词表里没有的标签原样保留、默认按 app 轴处理，
    所以新加标签不会因为忘了登记而消失——只是拿不到链接。
    """
    split = APP_TAGS.get('split', {})
    alias = APP_TAGS.get('alias', {})
    axis = APP_TAGS.get('axis', {})
    flat = []
    for t in tags:
        flat.extend(split.get(t, [t]))
    rows = {'app': [], 'measure': [], 'market': []}
    for t in flat:
        t = alias.get(t, t)
        k = axis.get(t, 'app')
        if t not in rows[k]:          # 归并后会出现重复（拆出来的燃气表与原有的燃气表）
            rows[k].append(t)
    return rows


def app_tag_rows(tags):
    """产品页的标签排。app 轴能配上案例页的渲染成 <a>，其余保持纯文字。

    分三排而不是一排：这三类词对应三种搜索意图——搜「位移检测传感器」的人要品类页，
    搜「燃气表 霍尔」的人要方案页，搜「汽车级」的人在筛市场。混在一排，
    点进去的人有一半会觉得走错地方。
    """
    rows = normalize_app_tags(tags)
    out = ''
    for key, label in (('app', '典型应用'), ('measure', '测量类型'), ('market', '面向市场')):
        items = rows[key]
        if not items:
            continue
        cells = ''
        for t in items:
            href = None
            if key == 'app':
                for a in APPS:
                    href = case_page_route(a['key'], t)
                    if href:
                        break
            # 没有案例页就不做链接：链到空壳页算 thin content，用户点一次也不会点第二次
            cells += f'<a href="{href}">{E(t)}</a>' if href else f'<span>{E(t)}</span>'
        out += chr(10) * 2 + f'<div class="c-tags c-tags--lg"><b>{label}</b>{cells}</div>'
    return out


def case_link(a, cse):
    """案例卡片优先进案例详情页，没有文案时退回推荐芯片页。"""
    return case_page_route(a['key'], cse['title']) or case_route(cse) or '/products/'


def render_case_pages():
    n = 0
    for a in APPS:
        ac = COPY.get('applications', {}).get(a['key'], {})
        for idx, cse in enumerate(a['cases']):
            slug, d = case_entry(a['key'], cse['title'])
            if not d:
                continue
            route = f'/applications/{a["key"]}/{slug}'
            chip_route = case_route(cse)
            chip_slug = chip_route.rsplit('/', 1)[-1] if chip_route else ''
            cp = pc(chip_slug) if chip_slug in PRODUCTS else None
            out = fm(title=f'{d["title"]} · {a["name"]}应用', description=d.get('lead', ''), aside=False,
                     pageClass='c-page c-page--case')
            out += eyebrow(HOME, (SEC['applications'], '/applications/'), (a['name'], f'/applications/{a["key"]}'), (d['title'], None))
            out += f'<p class="c-kicker">{E(a["name"])}</p>\n\n# {d["title"]}\n\n'
            out += f'<p class="c-lead">{E(d.get("lead", ""))}</p>\n\n'
            out += ('<div class="c-actions">'
                    + (f'<a class="c-btn c-btn--brand" href="{chip_route}">推荐芯片 {E(cse["chip"])}</a>' if chip_route else '')
                    + '<a class="c-btn" href="/contact">方案咨询</a></div>\n\n')

            img = IMG.get(f'case/{a["key"]}/{idx}')
            out += section('场景说明')
            body = '\n\n'.join(d.get('scenario') or [])
            if img:
                out += (f'<div class="c-split c-split--overview"><div class="c-split__text">\n\n{body}\n\n</div>'
                        f'<div class="c-split__media c-split__media--frame c-split__media--case"><img src="{img}" alt="{E(d["title"])}" loading="lazy"></div></div>\n\n')
            else:
                out += body + '\n\n'

            if d.get('requirements'):
                out += section('检测需求', f'{d["title"]}对传感器的主要要求。')
                out += '<div class="c-features">' + ''.join(
                    f'<div class="c-feature"><span class="c-feature__no">{i:02d}</span><div><h3>{E(r["title"])}</h3><p>{E(r["desc"])}</p></div></div>'
                    for i, r in enumerate(d['requirements'], 1)) + '</div>\n\n'

            if d.get('why_chip'):
                out += section(f'为什么选 {cse["chip"]}', (cp['lead'] if cp else ''))
                out += '<div class="c-features">' + ''.join(
                    f'<div class="c-feature"><span class="c-feature__no">{i:02d}</span><div><h3>{E(w["title"])}</h3><p>{E(w["desc"])}</p></div></div>'
                    for i, w in enumerate(d['why_chip'], 1)) + '</div>\n\n'
                if cp and chip_route:
                    out += grid([card(chip_route, product_visual(chip_slug), cp['name'], cp['lead'], kicker=cp['model'],
                                      media_kind='icon' if icon(chip_slug) else 'product', more='查看产品')], 2)

            if d.get('design_notes'):
                out += section('设计注意点', '通用工程建议，实际设计以产品手册与实测为准。')
                out += '<ul class="c-checklist">' + ''.join(f'<li>{E(x)}</li>' for x in d['design_notes']) + '</ul>\n\n'

            rel = [r for r in (d.get('related') or []) if r in (CASES.get(a['key']) or {})]
            if rel:
                out += section('相关案例')
                cards = []
                for rslug in rel[:4]:
                    rd = CASES[a['key']][rslug]
                    ridx = next((i for i, c2 in enumerate(a['cases']) if c2['title'] == rd['title']), None)
                    cards.append(card(f'/applications/{a["key"]}/{rslug}', IMG.get(f'case/{a["key"]}/{ridx}') if ridx is not None else '',
                                      rd['title'], rd.get('lead', ''), kicker=rd.get('chip', ''), media_kind='case', more='查看案例'))
                out += grid(cards, 4)
            out += cta()
            write(route.lstrip('/') + '.md', out)
            n += 1
    return n


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
        g = APP_GUIDES.get(a['key'], {})
        if g.get('intro'):
            out += '\n\n'.join(g['intro']) + '\n\n'
        if g.get('needs'):
            out += section('领域需求', f'{a["name"]}对磁传感器的共性要求。')
            out += '<div class="c-features">' + ''.join(
                f'<div class="c-feature"><span class="c-feature__no">{i:02d}</span><div><h3>{E(x["title"])}</h3><p>{E(x["desc"])}</p></div></div>'
                for i, x in enumerate(g['needs'], 1)) + '</div>\n\n'
        out += section('应用案例', ac.get('desc', ''))
        out += grid([card(case_link(a, cse), IMG.get(f'case/{a["key"]}/{n}'), cse['title'], kicker=cse['chip'],
                          media_kind='case', more='查看案例') for n, cse in enumerate(a['cases'])], 4)
        out += section('推荐芯片一览')
        out += '<div class="c-table c-table--links"><table><thead><tr><th>推荐芯片</th><th>对应产品</th><th>应用场景</th></tr></thead><tbody>'
        for (chip, route), titles in chips.items():
            slug = route.rsplit('/', 1)[-1] if route else ''
            prod = f'<a href="{route}">{E(pc(slug)["model"])} {E(pc(slug)["name"])}</a>' if slug in PRODUCTS else '—'
            out += f'<tr><td class="c-mono">{E(chip)}</td><td>{prod}</td><td>{E("、".join(titles))}</td></tr>'
        out += '</tbody></table></div>\n\n'
        if g.get('chip_map'):
            out += section('需求与芯片对照')
            out += '<div class="c-table c-table--links"><table><thead><tr><th>需求</th><th>推荐系列</th><th>依据</th></tr></thead><tbody>'
            for row in g['chip_map']:
                ser = row['series']
                sl = next((x for x in PRODUCTS if pc(x)['model'] == ser), '')
                cell = f'<a href="{PRODUCTS[sl]["route"]}">{E(ser)}</a>' if sl else E(ser)
                out += f'<tr><td>{E(row["need"])}</td><td>{cell}</td><td>{E(row["why"])}</td></tr>'
            out += '</tbody></table></div>\n\n'
        if g.get('checklist'):
            out += section('设计自检', '方案定型前先回答这几个问题。')
            out += '<ul class="c-checklist">' + ''.join(f'<li>{E(x)}</li>' for x in g['checklist']) + '</ul>\n\n'
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
        f'<div class="c-pillar"><span class="c-pillar__icon"><img src="{x["icon"]}" alt="{E(x["title"])}"></span><h3>{E(x["title"])}</h3></div>' for x in sv['strengths']) + '</div>\n\n'
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


# ---------- 技术基础 ----------
def render_glossary():
    g = GLOSSARY
    if not g.get('terms'):
        return 0
    terms = g['terms']
    out = fm(title='技术基础', description='产品页用到的角度测量、精度、接口与磁敏原理术语解释。', aside=False, pageClass='c-page')
    out += header([HOME, ('技术基础', None)], '技术基础',
                  '产品页里反复出现的术语，在这里统一解释：怎么装、精度怎么算、接口怎么选、几种磁敏原理有什么区别。',
                  [dict(value=len(g.get('groups', [])), label='主题'), dict(value=len(terms), label='术语')], kicker=BRAND)
    for grp in g.get('groups', []):
        out += section(grp['title'])
        for key in grp['terms']:
            d = terms.get(key)
            if not d:
                continue
            out += f'<h3 id="{key}">{E(d["term"])}</h3>\n\n'
            out += f'<p class="c-term-short">{E(d.get("short", ""))}</p>\n\n'
            out += '\n\n'.join(d.get('body') or []) + '\n\n'
            if d.get('note'):
                out += f'<p class="c-note">{E(d["note"])}</p>\n\n'
            rel = [x for x in (d.get('related_series') or [])]
            if rel:
                links = []
                for ser in rel:
                    sl = next((x for x in PRODUCTS if pc(x)['model'] == ser), '')
                    links.append(f'<a href="{PRODUCTS[sl]["route"]}">{E(ser)}</a>' if sl else E(ser))
                out += '<p class="c-term-rel"><b>相关系列</b>' + '、'.join(links) + '</p>\n\n'
    out += cta('还有拿不准的参数？', '选型、磁路与接口对接上的问题，欢迎直接找我们的技术团队确认。')
    write('basics.md', out)
    return len(terms)


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
    # 每一条地址都出一张卡（含没有地图图片的南京、杭州），点开进高德地图
    photo_of = {c2['name']: IMG.get(f'city/{n}', c2['image']) for n, c2 in enumerate(ct['cities'])}
    cards = []
    for b in groups:
        for item in b['items']:
            city, _, addr = item.partition('：')
            if not addr:
                city, addr = '', item
            city = city.replace('公司', '').strip()
            city = next((k for k in photo_of if k and k in item), city)
            img = photo_of.get(city, '')
            href = 'https://uri.amap.com/search?keyword=' + urllib.parse.quote(addr or item)
            cards.append(
                f'<a class="c-city{"" if img else " c-city--noimg"}" href="{href}" target="_blank" rel="noopener">'
                + (f'<img src="{img}" alt="{E(city)}地图" loading="lazy">' if img else '')
                + f'<figcaption><b>{E(city or b["name"])}</b><span>{E(b["name"])}</span><p>{E(addr or item)}</p>'
                  '<em>在高德地图中打开 →</em></figcaption></a>')
    out += grid(cards, 3)
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
def short_name(name):
    """侧边栏用的短名：去掉位数与泛泛的修饰词，保留能区分的部分。"""
    t = re.sub(r'^\s*\d+\s*(位|bit)\s*', '', str(name))
    for w in ('高精度', '高分辨率', '超灵敏', '微功耗', '低延时', '高速', '高性能', '低功耗'):
        t = t.replace(w, '')
    t = re.sub(r'\s+', ' ', t).strip()
    return t if len(t) <= 12 else t[:12]


def render_nav():
    prod_items = [{'text': f"{SEC['products']}总览", 'link': '/products/'}]
    side_products = [{'text': f"{SEC['products']}总览", 'link': '/products/'}]
    for c in CATS:
        slugs = [i['slug'] for i in c['items']] + [s for s, p in PRODUCTS.items() if p['category'] == c['key'] and s not in ITEM_BY_SLUG]
        prod_items.append({'text': c['name'], 'items': [{'text': f'{pc(s)["model"]} · {pc(s)["name"]}', 'link': PRODUCTS[s]['route']} for s in slugs]})
        side_items = [{'text': f'{c["name"]}总览', 'link': f'/products/{c["key"]}/'}]
        for sl in slugs:
            entry = {'text': f'{pc(sl)["model"]} {short_name(pc(sl)["name"])}', 'link': PRODUCTS[sl]['route']}
            mods = MODEL_INDEX.get(sl) or []
            if mods:
                entry['collapsed'] = True
                entry['items'] = [{'text': mid, 'link': route} for mid, route, _ in mods]
            side_items.append(entry)
        side_products.append({'text': c['name'], 'collapsed': False, 'items': side_items})
    apps = [{'text': f"{SEC['applications']}总览", 'link': '/applications/'}] + [{'text': a['name'], 'link': f'/applications/{a["key"]}'} for a in APPS]
    nav = [
        {'text': SEC['products'], 'activeMatch': '^/products/', 'items': prod_items},
        {'text': SEC['applications'], 'activeMatch': '^/applications/', 'items': apps},
        {'text': '服务与洞见', 'activeMatch': '^/(services|tech-talks)', 'items': [
            {'text': SEC['services'], 'link': '/services'}, {'text': SEC['techtalks'], 'link': '/tech-talks'},
            {'text': '技术基础', 'link': '/basics'}]},
        {'text': SEC['about'], 'activeMatch': '^/(about|contact)', 'items': [
            {'text': '公司简介', 'link': '/about/#公司简介'}, {'text': '核心价值观', 'link': '/about/#核心价值观'},
            {'text': '品质认证', 'link': '/about/#品质认证'}, {'text': '加入我们', 'link': '/about/#加入我们'},
            {'text': SEC['contact'], 'link': '/contact'}]},
    ]
    json.dump({'nav': nav, 'products': side_products, 'applications': apps},
              open(os.path.join(DOCS, '.vitepress', 'sidebar.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def prune_stale():
    """删掉上一轮生成、这一轮不再存在的页面（例如型号拆分后留下的旧文件）。"""
    n = 0
    for dirpath, dirnames, filenames in os.walk(DOCS):
        if '.vitepress' in dirpath or os.path.join('docs', 'public') in dirpath:
            continue
        for fn in filenames:
            if not fn.endswith('.md'):
                continue
            full = os.path.normcase(os.path.abspath(os.path.join(dirpath, fn)))
            if full not in WRITTEN:
                os.remove(os.path.join(dirpath, fn))
                n += 1
    for dirpath, dirnames, filenames in os.walk(DOCS, topdown=False):
        if '.vitepress' in dirpath or os.path.join('docs', 'public') in dirpath:
            continue
        if not os.listdir(dirpath) and os.path.abspath(dirpath) != os.path.abspath(DOCS):
            os.rmdir(dirpath)
    return n


def main():
    n_models = 0
    for slug in ORDER:
        render_product(slug)
        m = merged_matrix(slug, SPECS.get(slug) or [], figures_for(slug, PRODUCTS[slug]['figures'])[0])
        if m:
            n_models += len(render_model_pages(slug, m))
    render_products()
    render_applications()
    n_cases = render_case_pages()
    render_services()
    render_techtalks()
    n_terms = render_glossary()
    render_about()
    render_contact()
    render_home()
    render_nav()
    stale = prune_stale()
    print('rendered', len(PRODUCTS), 'products +', n_models, 'model +', n_cases, 'case pages +', n_terms,
          'terms + index pages; removed', stale, 'stale files')


if __name__ == '__main__':
    main()
