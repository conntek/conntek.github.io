# QA：元数据 / SEO / 可访问性审计

**审计时间**：2026-09-16
**审计范围**：`docs/**/*.md` 全部 159 篇（35 篇栏目页 + 124 篇型号页）、`docs/.vitepress/config.mts`、`docs/.vitepress/theme/style.css`（1608 行）
**判据**：静态解析每篇 md 的 frontmatter、标题层级、`<img>`/`<a>`/`<table>` 标签；`docs/public` 下逐个核对 src 是否存在；对 `style.css` 深色调色板按 WCAG 2.x 相对亮度公式算对比度。`npm run docs:dev` 在 dev 模式下只返回 SPA 外壳（`<title>` 为空是 dev 的正常表现），所以 head 的最终产物**没有**通过跑构建来核对，下面关于 head 的结论是从 config 与 frontmatter 推的。

---

## 摘要

总体是一份质量相当高的生成站：**零缺失 title/description、零重复 title、零空标题、每页恰好一个 H1、零标题层级跳跃、零失效内链、零失效图片 src、零指向 conntek.com.cn 页面的链接、18 条外链全部带 `target="_blank" rel="noopener"`。** 生成器把该做对的结构性东西基本都做对了。

问题集中在三块：

1. **型号页 description 撞车**——124 篇型号页里 **114 篇**的 description 与至少一篇别的页面逐字相同（24 个重复组，最大一组 15 篇）。根因是 `model_lead()` 只用「系列名 + 等级 + 封装 + 接口 + 供电」拼串，**唯独不带型号本身**，而同封装同接口的型号一抓一大把。这是本次唯一的搜索引擎级硬伤。
2. **表格语义与键值表**——427 张表，`<th>` 一个 `scope` 都没有（1834 个），一张 `<caption>` 都没有；`.c-table` 是 `overflow-x: auto` 但没有 `tabindex`，键盘用户无法滚动宽表。
3. **深色下的三级文字对比度**——`--vp-c-text-3: #6a6a71` 在 `#1b1b1f` 上只有 **3.20:1**，在 `--vp-c-bg-soft` 上 **2.99:1**，8 处用它当正文色（面包屑、`.c-muted` 等），未达 4.5:1。

其余多为廉价可修项，且绝大多数改在 `scripts/render.py` 的一两个函数里就能一次覆盖全部 159 页。

**一句话统计**：P0 4 项 / P1 8 项 / P2 6 项。

---

## P0 —— 必须修

### P0-1　114 篇型号页 description 逐字重复（24 组）

**文件**：`docs/products/**/*.md`（型号页），生成于 `scripts/render.py` 的 `model_lead()`（第 741 行附近）与 `render_model_pages()`（第 753 行）

**证据**（重复组按页数排序，取前几组）：

| 页数 | description | 代表文件 |
|---|---|---|
| 15 | `KTM13 系列 TMR 磁阻开关：锁存型级、SOT-23-3L / TO-92S 封装、CMOS 输出接口、1.8 ~ 5.5 V 供电电压` | `docs/products/switch/ktm13/ktm1331ma.md` 等 15 篇 |
| 15 | `KTM13 系列 TMR 磁阻开关：全极型级、SOT-23-3L / TO-92S 封装、CMOS 输出接口、1.8 ~ 5.5 V 供电电压` | `docs/products/switch/ktm13/ktm1301ma.md` 等 15 篇 |
| 10 | `KTM13 系列 TMR 磁阻开关：全极型级、SOT-23-3L / TO-92S 封装、开漏输出 输出接口、1.8 ~ 5.5 V 供电电压` | `docs/products/switch/ktm13/ktm1302sa.md` 等 10 篇 |
| 9 | `KTH16 系列 微功耗 1D 霍尔开关：全极型级、SOT-23-3L / TO-92S 封装、CMOS 输出接口、1.8 ~ 5.5 V 供电电压` | `docs/products/switch/kth16/kth1701fh.md` 等 9 篇 |
| 8 | `KTM13 系列 TMR 磁阻开关：单S极级…` / `…单N极级…` | `ktm1311sa.md` / `ktm1321sa.md` 各 8 篇 |
| 6 | `KTH31 系列 比例式线性霍尔传感器：SOT-23 / TO-92S / DFN1616 封装、模拟电压输出 输出接口、3.0 ~ 5.5 V 供电电压` | `docs/products/switch/kth31/kth3101.md` 等 6 篇 |

合计 **114/124 = 92%** 的型号页 description 不唯一。同时注意这批页面的 `<p class="c-lead">` 用的是同一个字符串，所以**页面可见的首屏导语也一样**——不只是 meta 层面的问题。

**为什么严重**：这 114 篇的正文主体是「参数详情」键值表，本来就高度同构；再叠加一模一样的 description，搜索引擎极可能只收录每组中的一篇，其余判为重复内容。这正好打掉了「一型号一页」这个建站决策的全部收益。

**修法**（改 `model_lead()`，让型号本身与真正区分同组型号的那一两个参数进串）：

```python
# scripts/render.py —— 替换现有 model_lead()
# 每个组内真正不同的参数：开关看磁场阈值，编码器看分辨率/精度/转速
DIFF_FIELDS = ['磁场阈值', 'Bop', 'Brp', '工作磁场', '灵敏度',
               '分辨率', '精度', '角度 INL', '非线性误差', '转速', '噪声（1σ）']


def model_lead(series_name, grade, fields, mid=''):
    bits = []
    if grade:
        bits.append(f'{grade}级')
    for n in ('封装', '输出接口', '供电电压'):
        if fields.get(n) and fields[n] != '—':
            bits.append(f'{fields[n]} 封装' if n == '封装' else f'{fields[n]} {n}')
    # 关键：补 1~2 个组内真正不同的参数，保证 description 唯一
    for n in DIFF_FIELDS:
        v = fields.get(n)
        if v and v != '—' and len(bits) < 6:
            bits.append(f'{n} {v}')
    head = f'{mid} {series_name}'.strip() if mid else series_name
    return head + ('：' + '、'.join(bits) if bits else '')
```

`render_model_pages()` 里三处调用都补上 `mid=`（第 753、756 行的 description 与 `c-lead`；第 792 行左右的同系列卡片可以不带）：

```python
lead = model_lead(c['model'] + ' ' + c['name'], grade, fields, mid=mid)
out = fm(title=f'{mid} · {c["model"]}{c["name"]}', description=lead,
         aside=False, pageClass='c-page c-page--model')
...
out += f'<p class="c-lead">{E(lead)}</p>\n\n'
```

**跑完必须复核唯一性**（加进生成流程当门禁）：

```python
# render.py 末尾
seen = {}
for root, _, fs in os.walk(DOCS):
    for f in fs:
        if f.endswith('.md'):
            t = open(os.path.join(root, f), encoding='utf-8').read()
            m = re.search(r'^description: (.*)$', t, re.M)
            if m:
                seen.setdefault(m.group(1), []).append(f)
dups = {k: v for k, v in seen.items() if len(v) > 1}
assert not dups, f'重复 description {len(dups)} 组：{list(dups.values())[:3]}'
```

---

### P0-2　2 篇型号页的 title / H1 / 面包屑里嵌了换行符

**文件**：
- `docs/products/switch/linear-hall/kth5641a1-kth5641a2-kth5641a3-kth5641a4.md`
- `docs/products/switch/linear-hall/kth5643a1-kth5643a2-kth5643a3-kth5643a4.md`

**证据**（`cat -A` 原样）：

```
title: "KTH5641A1\nKTH5641A2\nKTH5641A3\nKTH5641A4 · KTH564 系列线性霍尔芯片"
...
<span>KTH5641A1
KTH5641A2
KTH5641A3
KTH5641A4</span></nav>

# KTH5641A1
KTH5641A2
KTH5641A3
KTH5641A4
```

三处坏掉：① YAML 双引号串里的 `\n` 会被解析成真换行，进 `<title>` 就是一个带换行的标题，算上 `titleTemplate` 后缀共 71 字符，超 60；② markdown 的 ATX 标题只吃第一行，所以 **H1 实际只有 `KTH5641A1`**，后面三个型号掉成了一个裸段落；③ 面包屑最后一节变成四行。

**根因**：`cache/site.json` 的型号矩阵里，某些单元格把四个型号塞在一格并用换行分隔；`render_model_pages()` 的 `mid = str(row[0]).strip()` 只去首尾空白，不处理中间的换行。

**修法**（`scripts/render.py`，`render_model_pages()` 里取 `mid` 的那一行）：

```python
# 旧： mid = str(row[0]).strip()
mid = re.sub(r'\s*[\r\n]+\s*', ' / ', str(row[0])).strip()
```

这样标题变成 `KTH5641A1 / KTH5641A2 / KTH5641A3 / KTH5641A4`，H1 完整、面包屑单行。若嫌太长，可在 `fm(title=...)` 处再做一次压缩：

```python
short = mid if len(mid) <= 24 else mid.split(' / ')[0] + f' 等 {len(mid.split(" / "))} 个型号'
out = fm(title=f'{short} · {c["model"]}{c["name"]}', description=lead, ...)
```

（另：`model_slug()` 对这个多行 mid 生成的路由 `kth5641a1-kth5641a2-kth5641a3-kth5641a4` 本身没坏，但换成 `/` 后 slug 不变，路由稳定，不会断链。）

---

### P0-3　没有 sitemap，config 里完全没有 `sitemap` 字段

**文件**：`docs/.vitepress/config.mts`；`docs/public/` 下也没有 `sitemap.xml` 与 `robots.txt`

**证据**：`grep -n "sitemap" docs/.vitepress/config.mts` 零命中；`ls docs/public/*.xml docs/public/*.txt` 无输出。

159 个页面、124 个型号页全靠内链被爬。VitePress 1.x 内置 sitemap，只要给 hostname 就会在构建时产出 `dist/sitemap.xml`。

**修法**（`docs/.vitepress/config.mts`，加在 `cleanUrls` 旁边）：

```ts
  cleanUrls: true,
  sitemap: {
    hostname: 'https://conntek.github.io/msite/',
    transformItems: (items) =>
      items.map((i) => ({
        ...i,
        changefreq: 'monthly',
        priority: i.url === '' ? 1.0 : i.url.startsWith('products/') ? 0.8 : 0.6,
      })),
  },
```

配套在 `docs/public/robots.txt` 新建：

```
User-agent: *
Allow: /

Sitemap: https://conntek.github.io/msite/sitemap.xml
```

⚠️ hostname 必须与实际部署域一致，换域时和 `SITE_BASE` 一起改。

---

### P0-4　没有任何 og: / twitter: 社交卡片 meta

**文件**：`docs/.vitepress/config.mts`（`head` 数组只有 icon 与 theme-color 两条）

**证据**：

```ts
  head: [
    ['link', { rel: 'icon', type: 'image/png', href: `${base}img/logo-nav-light.png` }],
    ['meta', { name: 'theme-color', content: '#c30d23' }],
  ],
```

微信、钉钉、企微、LinkedIn 转发这批产品页时抓不到标题图与摘要，只能显示裸链接。芯片选型页大量走 IM 转发，这条的实际损失不小。

**修法**（用 `transformPageData` 逐页注入，能吃到每页自己的 title/description）：

```ts
const HOST = 'https://conntek.github.io'

export default defineConfig({
  // …existing config…
  transformPageData(pageData) {
    const title =
      (pageData.frontmatter.title as string | undefined)?.replace(/\s*[\r\n]+\s*/g, ' / ') ??
      pageData.title ??
      '昆泰芯微电子'
    const desc =
      (pageData.frontmatter.description as string | undefined) ??
      '昆泰芯微电子 · 智能感知世界 传递美好生活'
    const url = `${HOST}${base}${pageData.relativePath.replace(/((^|\/)index)?\.md$/, '$2')}`

    pageData.frontmatter.head ??= []
    pageData.frontmatter.head.push(
      ['meta', { property: 'og:type', content: 'website' }],
      ['meta', { property: 'og:site_name', content: '昆泰芯微电子 CONNTEK' }],
      ['meta', { property: 'og:locale', content: 'zh_CN' }],
      ['meta', { property: 'og:title', content: `${title} · 昆泰芯 CONNTEK` }],
      ['meta', { property: 'og:description', content: desc }],
      ['meta', { property: 'og:url', content: url }],
      ['meta', { property: 'og:image', content: `${HOST}${base}img/ref/hero-magnet-sensor-render.png` }],
      ['meta', { property: 'og:image:width', content: '1088' }],
      ['meta', { property: 'og:image:height', content: '964' }],
      ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
      ['link', { rel: 'canonical', href: url }],
    )
  },
})
```

（`og:image` 用 `.png` 而非 `.webp`：部分 IM 的抓取器不认 webp。`hero-magnet-sensor-render.png` 实测存在，尺寸 1088×964。想更好看的话另出一张 1200×630 放 `docs/public/img/ref/og-default.png`。）

---

## P1 —— 该修

### P1-1　1834 个 `<th>` 没有 `scope`，427 张表没有 `<caption>`

**文件**：`scripts/render.py` 的 `render_model_pages()`（键值表，第 770 行附近）、`spec_entry()` / `transposed_table()` / `docs_table()`

**证据**：132 篇页面的「参数详情」键值表共 1834 个 `<th>`，全部形如 `<th>系列</th><td>KTH7111</td>`。这类表一行两组键值，屏幕阅读器无法把 `<td>` 关联回左边的 `<th>`，读出来就是一串孤立数值。全站 427 张表零 `<caption>`。

（说明：审计脚本报「132 张表没有 `<thead>`」，逐张核对后判定**不是缺陷**——这些是键值表，本来就没有列头行，正确的修法是加 `scope="row"` 而不是硬塞 `<thead>`。）

**修法**（`render_model_pages()` 里拼键值表的那段）：

```python
out += f'<div class="c-table c-kv"><table><caption class="c-tbl-cap">{E(mid)} 参数详情</caption><tbody>'
for i in range(0, len(items), 2):
    out += '<tr>'
    for n, v in items[i:i + 2]:
        out += f'<th scope="row">{E(n)}</th><td>{cell_html(v)}</td>'
    if len(items[i:i + 2]) == 1:
        out += '<th scope="row"></th><td></td>'
    out += '</tr>'
out += '</tbody></table></div>\n\n'
```

列头型表（`transposed_table()` / `docs_table()` / `spec_entry()`）里 `<thead>` 中的 `<th>` 加 `scope="col"`，`<tbody>` 行首的加 `scope="row"`。`style.css` 补一条把 caption 视觉隐藏但保留给读屏（因为章节标题里已经写过一遍，视觉上重复）：

```css
.c-table caption {
  position: absolute;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
}
```

---

### P1-2　`.c-table` 可横向滚动但键盘够不着

**文件**：`docs/.vitepress/theme/style.css:489`

**证据**：

```css
.c-table {
  margin: 20px 0;
  overflow-x: auto;
  ...
}
```

「同系列对比」的转置表最多 6 列，在手机上必然横向溢出。`overflow-x: auto` 的容器若不可聚焦，只能用鼠标/触屏拖动，纯键盘用户读不到右侧列（WCAG 2.1.1）。

**修法**（`render.py` 里所有产出 `<div class="c-table…">` 的地方统一加属性，最省事是包一层函数）：

```python
def table_wrap(inner_html, label, extra_cls=''):
    return (f'<div class="c-table{extra_cls}" role="region" tabindex="0" '
            f'aria-label="{E(label)}">' + inner_html + '</div>\n\n')
```

并在 `style.css` 给聚焦态一个可见轮廓（见 P1-6）。

---

### P1-3　18 张内容图 `alt=""`

**证据**（全站 444 张 `<img>`，388 张 `alt=""`；其中 370 张是卡片/行内的装饰图标，紧邻同义可见文字，`alt=""` **判定正确、不用改**。真正有问题的是这 18 张）：

| 文件 | 数量 | src | 性质 |
|---|---|---|---|
| `docs/products/knob/knob.md` | 10 | `/msite/images/kuntaikonb1.png` ~ `10.png` | 产品形态海报，**图上烤了文字**，且是唯一内容载体 |
| `docs/contact.md` | 4 | `/msite/img/city/0.webp` ~ `3.webp` | 城市照片（有 figcaption 写城市名，但照片本身是内容） |
| `docs/services.md` | 3 | `/msite/images/dianlusheji.png`、`cilusheji2.png`、`jiegousheji.png` | 能力支柱图标（84×84 容器，60×72 原图），旁边有 `<h3>` 文字 |

`services.md` 那 3 张严格说是装饰（h3 已给出同样信息），可以保留 `alt=""`；**必须修的是 knob 的 10 张海报和 contact 的 4 张城市图**。

**修法一**（`render.py:631`，海报）：

```python
out += '<div class="c-gallery c-gallery--posters">' + ''.join(
    f'<a href="{i}" target="_blank" rel="noopener">'
    f'<img src="{i}" alt="{E(c["model"])} 产品形态示例 {n + 1}：{E(os.path.basename(i))}" loading="lazy"></a>'
    for n, i in enumerate(imgs)) + '</div>\n\n'
```

更好的做法是在 `content/figures.json` 里像现有 diagram 条目那样给这 10 张各写一句 `caption`（该文件已有 `kind`/`caption`/`used_by` 结构，直接复用），然后 alt 取 caption。

**修法二**（`render.py:1114`，城市图）：

```python
out += grid([f'<figure class="c-city">'
             f'<img src="{IMG.get(f"city/{n}", c["image"])}" alt="{E(c["name"])}办公地点外景" loading="lazy">'
             f'<figcaption><b>{E(c["name"])}</b><span>{E(c["en"].title())}</span></figcaption></figure>'
             ...
```

---

### P1-4　knob 海报把 519×1400 的竖图压进 1:1 方框

**文件**：`docs/.vitepress/theme/style.css:636`（`.c-gallery img { aspect-ratio: 1; object-fit: contain; }`）+ `:1349`（`.c-gallery--posters { grid-template-columns: repeat(2, …) }`）

**证据**：`kuntaikonb1.png` 实测 519×1400（宽高比 1:2.7）。在 `aspect-ratio: 1` + `object-fit: contain` 下，图片按高度缩到方框内，实际渲染宽度只剩约 37% 的格宽。**这些海报上烤着产品规格文字，缩到这个尺寸完全读不了**——等于把内容藏起来了。

**修法**：给海报变体单独一套比例，别沿用通用画廊的 1:1：

```css
.c-gallery--posters {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}
.c-gallery--posters img {
  aspect-ratio: auto;      /* 覆盖 .c-gallery img 的 1 */
  max-height: 520px;
  object-fit: contain;
}
@media (max-width: 720px) {
  .c-gallery--posters { grid-template-columns: 1fr; }
}
```

**另外**：海报上的文字属于「该是真文本的图上文字」。`content/figures.json` 已经把 9 张表格图转写成了文字表（做得对），这 10 张海报是同一类欠账——长期方案是把海报上的规格转写进 `content/copy.json`，页面上用真表格，海报降为配图。

---

### P1-5　444 张 `<img>` 全部没有 `width`/`height`

**证据**：444/444。好消息是大部分容器已经用 CSS 兜住了比例，**真正会抖的只有三类容器**：

| 容器 | style.css | 有没有 aspect-ratio | CLS 风险 |
|---|---|---|---|
| `.c-card__media` | :241 | 有（4/3） | 无 |
| `.c-product-hero__media` | :404 | 有（4/3） | 无 |
| `.c-row__media` | :684 | 有（4/3） | 无 |
| `.c-city img` | :995 | 有（2/1） | 无 |
| `.c-gallery img` | :636 | 有（1） | 无 |
| **`.c-fig img`** | :605 | **没有**，只有 `max-height: 360px` | **有** |
| **`.c-cell-fig img`** | :546 | **没有**，只有 `max-height: 120px` | **有** |
| **`.c-split__media img`** | :901 | **没有**，只有 `width: 100%` | **有** |

`.c-fig` 装的是感应方向示意图（`content/figures.json` 里 12 张 diagram），`.c-split__media` 装的是产品概述配图——都在首屏偏上位置，加载前高度为 0，加载后撑开，正文往下跳。

**修法**（在 `render.py` 里直接写死真实尺寸，最彻底）。`scripts/images.py` 已经在生成派生图，顺手把宽高记进 `cache/img_manifest.json`，渲染时取用：

```python
# render.py 顶部
DIMS = load('cache/img_dims.json', {})   # {"/img/xxx.webp": [w, h]}


def img_tag(src, alt, cls='', lazy=True):
    wh = DIMS.get(src)
    attrs = f' width="{wh[0]}" height="{wh[1]}"' if wh else ''
    return (f'<img src="{src}" alt="{E(alt)}"{attrs}'
            + (f' class="{cls}"' if cls else '')
            + (' loading="lazy"' if lazy else '') + '>')
```

然后把 `card()`、`fig`、`c-split__media`、`c-cell-fig` 等处的手写 `<img …>` 全换成 `img_tag(...)`。配套在 `style.css` 加一条兜底，防止写死尺寸后图片在窄屏溢出：

```css
.vp-doc img { max-width: 100%; height: auto; }
```

**廉价版**（不改 render.py，只补 CSS，能解决三分之二）：

```css
.c-fig img        { aspect-ratio: 4 / 3; object-fit: contain; }
.c-cell-fig img   { aspect-ratio: 3 / 1; object-fit: contain; }
.c-split__media img { aspect-ratio: 4 / 3; object-fit: cover; }
```

---

### P1-6　全站没有任何 `:focus-visible` 样式

**证据**：`grep -n "focus" docs/.vitepress/theme/style.css` **零命中**。而 `.c-btn`、`.c-card`、`.c-link`、`.c-crumbs a` 全部是自定义样式的 `<a>`，`:hover` 写了（`border-color` + `color` 变 brand），`:focus` 一条没有。VitePress 默认主题的 base.css 只给 `button`/`input`/`textarea`/`select` 设了聚焦样式，**不覆盖 `<a>`**。纯键盘用户 Tab 过卡片网格时没有任何视觉反馈（WCAG 2.4.7）。

**修法**（`style.css` 末尾加一节）：

```css
/* ---------- 键盘聚焦 ---------- */
.vp-doc a.c-btn:focus-visible,
.vp-doc a.c-card:focus-visible,
.vp-doc a.c-link:focus-visible,
.c-crumbs a:focus-visible,
.c-gallery a:focus-visible,
.c-table[tabindex]:focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 3px;
  border-radius: var(--c-radius-sm);
}
```

`--vp-c-brand-1` 深色下是 `#ff5d6c`，对 `#1b1b1f` 有 5.75:1，做聚焦环够用（非文本对比只需 3:1）。

---

### P1-7　深色下 `--vp-c-text-3` 用作正文色，对比度 3.20:1 / 2.99:1

**文件**：`docs/.vitepress/theme/style.css:50`（token）、`:93`（`.c-crumbs`）、`:164`（`.c-muted`）、`:556`、`:869`、`:1009`、`:1167`、`:1299`

**实测对比度**（深色 `--vp-c-bg: #1b1b1f`、`--vp-c-bg-soft: #202127`，按 WCAG 相对亮度算）：

| 前景 / 背景 | 比值 | AA 正文 4.5:1 | AA 大字 3:1 |
|---|---|---|---|
| `--vp-c-text-1` `#dfdfd6` / `#1b1b1f` | **12.81:1** | 过 | 过 |
| `--vp-c-text-2` `#98989f` / `#1b1b1f` | **5.99:1** | 过 | 过 |
| **`--vp-c-text-3` `#6a6a71` / `#1b1b1f`** | **3.20:1** | **不过** | 过 |
| **`--vp-c-text-3` / `#202127`（bg-soft）** | **2.99:1** | **不过** | **不过** |
| `--vp-c-brand-1` `#ff5d6c` / `#1b1b1f` | 5.75:1 | 过 | 过 |
| `#fff` / `--vp-c-brand-3` `#c30d23`（主按钮） | 6.17:1 | 过 | 过 |
| `#fff` / `#a60b1e`（按钮 hover） | 7.81:1 | 过 | 过 |
| `#c30d23` / `#fff`（CTA 反白按钮） | 6.17:1 | 过 | 过 |
| `--vp-c-divider` `#2e2e32` / `#1b1b1f`（边框） | 1.27:1 | — | **不过**（非文本也需 3:1） |

最要紧的两处：`.c-crumbs` 是 13px 的面包屑（**小字**，必须 4.5:1），`.c-muted` 被 `render.py:524` 用在「（暂不可下载）」这种必须读到的状态文字上。

**修法**（`style.css` 深色块里只改这一个 token）：

```css
.dark {
  /* …其余不动… */
  --vp-c-text-3: #8a8a92;   /* 原 #6a6a71 → 对 #1b1b1f 4.77:1，对 #202127 4.46:1 */
}
```

想更稳一点用 `#909098`（对 `#1b1b1f` 5.26:1、对 `#202127` 4.92:1，两个底色都过 4.5:1）。

边框 `--vp-c-divider` 那条 1.27:1 是「非文本对比」，卡片边界在暗底上几乎看不见；若卡片本身有 `background` 与页面底色区分则可豁免，但本站 `--c-surface = --vp-c-bg`（与页面同色），所以**边框是卡片唯一的边界**——建议 `--vp-c-divider: #3d3d43` 起步。

---

### P1-8　本地搜索没有中文分词，基本搜不出东西

**文件**：`docs/.vitepress/config.mts`，`themeConfig.search` 只配了 `translations`

**证据**：`provider: 'local'` 底层是 MiniSearch，默认按空白/标点切词。中文正文没有空格，「磁编码器」「霍尔开关」这类词整段被当成一个 token，用户输入「编码器」**命中不了**「磁编码器」。站内 159 页、124 个型号，搜索是主要导航方式之一。

**修法**（加 `miniSearch` 选项，按单字切分 + 前缀匹配）：

```ts
    search: {
      provider: 'local',
      options: {
        miniSearch: {
          options: {
            // 中文按单字切，英文/型号号按非字母数字切
            tokenize: (text: string) =>
              text
                .split(/[^\p{L}\p{N}]+/u)
                .flatMap((w) => (/[一-龥]/.test(w) ? [w, ...w.split('')] : [w]))
                .filter(Boolean),
          },
          searchOptions: {
            prefix: true,
            fuzzy: 0.2,
            combineWith: 'AND',
            boost: { title: 4, titles: 2, text: 1 },
          },
        },
        translations: { /* …保持现有… */ },
      },
    },
```

---

## P2 —— 可以排后面

### P2-1　11 篇栏目页 description 偏短

**证据**（字符数）：`docs/products/other/index.md` 18 字、`intelligent-transportation.md` 19 字、`industry4.md` 20 字、`intelligent-life.md` 21 字、`3d-hall/index.md` 23 字、`consumer-electronics.md` 24 字、`knob/index.md` 26 字、`encoder/index.md` 27 字、`switch/index.md` 28 字、`about/index.md` 31 字、`knob/knob.md` 32 字。

**注意口径**：任务书给的 60–160 字符是**拉丁文**标准（按像素宽度折算）。中文一个字约占两个拉丁字符宽，Google 中文摘要实际截断在 **38~50 个汉字**左右。按这个口径重判：36 篇「短」里只有上面这 11 篇（< 35 字）确实偏短，**其余 25 篇（35~59 字符）其实正好**，不用动。

**修法**：在 `content/copy.json` 里给这 11 个页面的 `lead` 各补一句具体的产品线/应用词（别让生成器凭空造，`page_copy()` 本来就优先读 copy.json）。目标 40~50 字。

### P2-2　`href="#技术文档"` 未做百分号编码（130 处）

`render.py:730` 与 `:762` 生成 `<a class="c-btn c-btn--brand" href="#技术文档">`。VitePress 的 slugify 保留 CJK，所以**实际能跳**，但裸非 ASCII 片段在部分旧浏览器/抓取器上会被规范化得不一致。

```python
import urllib.parse
ANCHOR_DOCS = '#' + urllib.parse.quote('技术文档')
```

### P2-3　`tel:` 不是 E.164 格式（4 处）

`docs/contact.md`：`tel:0512-62982283`、`tel:0755-86006609`、`tel:0755-86186696`、`tel:18620321032`。手机上从境外或漫游状态点击拨不通。改成 `tel:+86-512-62982283`、`tel:+86-755-86006609`、`tel:+86-755-86186696`、`tel:+86-186-2032-1032`（显示文字可以保持现状不变，只改 href）。生成处在 `render_contact()`。

### P2-4　`.c-btn` 高度 40px，低于 44px 触摸目标建议值

`style.css:360` `.c-btn { height: 40px; padding: 0 18px; }`。WCAG 2.2 AA 的硬门槛是 24×24（过了），44×44 是 AAA / Apple HIG 建议。型号页首屏并排三个按钮，手机上误触概率不低。

```css
@media (max-width: 640px) {
  .vp-doc a.c-btn { height: 44px; padding: 0 20px; }
  .c-actions { gap: 12px; }
}
```

另：`.c-crumbs` 13px 的面包屑链接、`.c-card__more` 13px，都在 24px 以下的行高里，属于同类但优先级更低。

### P2-5　favicon 只有一个 PNG，没有 apple-touch-icon / 没有 manifest

`config.mts` 的 `head` 只有 `img/logo-nav-light.png` 一条 icon。补：

```ts
    ['link', { rel: 'apple-touch-icon', href: `${base}img/logo-nav-light.png` }],
    ['meta', { name: 'format-detection', content: 'telephone=no' }],
```

（`theme-color: #c30d23` 已有，正确。`lang: 'zh-CN'` 已有，正确。`cleanUrls: true` 已有，正确。）

### P2-6　`lastUpdated: false`，产品页没有任何时间信号

对芯片选型站，「这份参数是什么时候的」是读者的真实疑问，也是搜索引擎的新鲜度信号。但本站页面由脚本重渲染，git mtime 会把全部 159 页刷成同一天，开 `lastUpdated: true` 反而制造假信号。**建议不开 `lastUpdated`**，改为在 `render.py` 的 `docs_table()` 里给每份可下载文档标注手册版本号（数据源 `cache/site.json` 里若有版本字段），比页面时间戳更有信息量。

---

## 已核对并判定「没问题」的项（留档，免得下次重查）

| 项 | 结果 |
|---|---|
| frontmatter 缺 `title` | 0 篇 |
| frontmatter 缺 `description` | 0 篇 |
| 重复 `title` | **0 组**（124 个型号页 title 全唯一，因为带了 `mid`） |
| `title` 含占位符文本 | 0 |
| `description` 超 160 字符 | 0 篇 |
| 每页 H1 数量 ≠ 1 | **0 篇**（159/159 正好一个） |
| 空标题 | 0 |
| H2/H3 层级跳跃（含 HTML 标题） | **0 篇** |
| `<img>` 没有 `alt` **属性** | 0（444/444 都写了 alt，只是 388 个为空，其中 370 个空得正确） |
| `src` 在 `docs/public` 下不存在 | **0 张** |
| 内链失效 | **0 条** |
| 指向 `conntek.com.cn` **页面**的链接 | **0 条**（642 处 `conntek.com.cn` 全部是 `mailto:` 里的邮箱域名，符合要求） |
| 外链缺 `target` / `rel` | **0 条**（18 条 mp.weixin.qq.com 链接全部带 `target="_blank" rel="noopener"`，由 `card(external=True)` 统一加） |
| 宽表（≥8 列） | 0 张（最宽的「同系列对比」6 列，`MAX_COMPARE` 限住了） |
| `lang` / `cleanUrls` / `theme-color` / icon | 均已正确配置 |

---

## 修复优先级建议（按「改一处覆盖多少页」排）

| 序 | 项 | 改哪 | 覆盖 |
|---|---|---|---|
| 1 | P0-1 description 撞车 | `render.py` `model_lead()` 一个函数 | 114 页 |
| 2 | P0-3 sitemap | `config.mts` 加 6 行 | 全站 |
| 3 | P0-4 og meta | `config.mts` 加 `transformPageData` | 全站 |
| 4 | P1-7 对比度 | `style.css` 改 1 个 token | 全站 8 处 |
| 5 | P1-6 focus 样式 | `style.css` 加 1 节 | 全站 |
| 6 | P1-1 `scope` + `caption` | `render.py` 4 个建表函数 | 427 张表 |
| 7 | P0-2 换行标题 | `render.py` 一行正则 | 2 页 |
| 8 | P1-5 CLS | `style.css` 加 3 条（廉价版）或 `render.py` 加 `img_tag()`（彻底版） | 444 张图 |
| 9 | P1-8 中文搜索 | `config.mts` 加 `miniSearch` | 全站 |
| 10 | P1-3/P1-4 knob 海报 | `render.py:631` + `style.css:1349` | 1 页 14 张图 |
