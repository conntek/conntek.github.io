# 全站链接 / 结构 / 一致性巡检

**巡检时间**：2026-09-16 14:08
**巡检范围**：`docs/**/*.md`（195 篇，由 `scripts/render.py` 生成）+ `docs/.vitepress/dist`（196 个 html，含 `404.html`）+ `docs/public`（379 个资源）+ `docs/.vitepress/sidebar.json`
**判据**：md 源码里的 `<a href>` / markdown 链接 / frontmatter `link:` 全部提取，按 `base=/msite/`、`cleanUrls: true` 解析成页面 URL，再回查生成的 md 与 dist 里的 html；frontmatter 的 `link:`（home hero actions）由 VitePress `withBase` 自动加 base，不算缺前缀；资源按 `docs/public` 实际文件比对（URL 解码后比对，中文文件名不算漏）。
**注意**：巡检期间站点被重新渲染过两次（14:01、14:05），本报告对应 14:05 那一版产物。

## 汇总

| 项目 | 数 |
|---|---|
| 页面（md） | 195（19 系列页 / 134 型号页 / 5 产品线首页 / 1 产品中心 / 5 应用领域 / 25 应用案例 / 6 单页：首页·关于·基础知识·联系·服务·技术洞见） |
| dist html | 196（195 + `404.html`），**每一篇 md 都有对应 html** |
| 扫描的内部链接 | 7406 |
| 扫描的资源引用（img / video / poster / source） | 563 |
| **死链** | **4**（同样 4 条在 dist 里 404） |
| 锚点链接 | 141（全部是 `#技术文档`），**0 条失效** |
| `/files/...` 下载链接 | 80 个 PDF 全部命中，**0 缺失**；`docs/public/files` 里 80 个文件**全部被引用** |
| 缺失的图片 / 视频 | **0** |
| 未被引用的 public 资源 | **163**（见第 2.2 节） |
| 孤岛页面 | **0** |
| sidebar / nav 条目 | nav 33 + products 159 + applications 5，**全部可解析、dist 里都有 html** |
| 跨系列错放 | **2 个型号页**（另有 2 条表头链接指错系列页） |
| 正文完全相同的页面 | **0** |
| 正文近乎相同的页面对 | 518 对（其中 516 对是同系列型号变体，属设计使然）；**1 个型号被渲染成两份**（见第 7 节） |

---

## 1. 死链（4 条，dist 里同样 404）

根因只有一个：**参数对比表的表头把「一个单元格里写了多个型号」整格拿去做 slug，而型号页是按 `split_models()` 拆开后逐个生成的**，两边 slug 对不上。

| 文件 | 链接 | 证据 |
|---|---|---|
| `docs/products/switch/ktm28.md` | `/msite/products/switch/ktm28/ktm2801-ktm2802` | 表头文字是 `KTM2801 / KTM2802`；实际生成的是 `ktm28/ktm2801.md` 与 `ktm28/ktm2802.md` |
| `docs/products/switch/linear-hall.md` | `/msite/products/switch/linear-hall/kth5641a1-kth5641a2-kth5641a3-kth5641a4` | 表头文字是 `KTH5641A1<br>KTH5641A2<br>KTH5641A3<br>KTH5641A4`；实际页面是 `kth5641a1.md` ~ `kth5641a4.md` |
| `docs/products/switch/linear-hall.md` | `/msite/products/switch/linear-hall/kth5642a1-kth5642a2` | 同上，实际是 `kth5642a1.md` / `kth5642a2.md` |
| `docs/products/switch/linear-hall.md` | `/msite/products/switch/linear-hall/kth5643a1-kth5643a2-kth5643a3-kth5643a4` | 同上，实际是 `kth5643a1.md` ~ `kth5643a4.md` |

**render.py 修法**：`transposed_table()` 的 `head_cell()`（约 252~256 行）现在写的是

```python
inner = f'<a href="{model_link(prod, h)}">{inner}</a>'
```

`h` 是原始单元格文本。改成按 `split_models(h)` 拆开后逐个型号加链接（每个型号名各自是一个 `<a>`，`<br>` 保留在外面），或者退一步只链第一个型号 `model_link(prod, split_models(h)[0])`。前者更好，因为读者点哪个型号就该进哪个型号页。

**顺带**：`render_model_pages()`（约 938 行）用 `split_models(row[0])` 展开，和 `head_cell` 用整格文本，这两处对「型号单元格」的解释必须统一——建议把「一格 → 型号列表」收敛成一个函数，表头和型号页都调它。

---

## 2. 资源

### 2.1 缺失资源：0

563 处 `<img src>` / `<video src>` / `poster=` / markdown 图片、80 处 `/files/*.pdf` 下载链接，全部在 `docs/public` 下找得到实体文件（含中文名 PDF，如 `KTH4603 Series产品手册.pdf`，URL 里是百分号编码，解码后命中）。`docs/public/videos` 下 6 个 mp4 也全部被引用。

### 2.2 未被引用的资源：163

这些文件躺在 `docs/public` 但全站没有一处链接，属于死重量（`dist` 会原样拷贝，拖大仓库和部署包）。

| 目录 | 个数 | 判断 |
|---|---|---|
| `/images/**`（含 `images/tech-talk` 16、`images/ext` 1） | 114 | 早年 `scripts/crawl.py` 抓下来的旧站素材，现站点改用 `/img/**`，整棵树已无人引用 |
| `/img/hero/*.webp` | 19 | `product_visual()`（render.py 约 77 行）的取值顺序是 `icon(slug) or IMG['prod/..'] or IMG['hero/..']`，19 个系列现在都有 `icons-web` 图标，`hero/` 这一档永远轮不到 |
| `/img/prod/*.webp` | 18 | 同上，被 `icons-web` 挤掉 |
| `/img/cat/*.webp` | 5 | 产品线卡片已改用 `icons-web/cat-*.webp` |
| `/img/logo-dark.png`、`/img/logo-light.png` | 2 | 导航实际用的是 `logo-nav-dark.png` / `logo-nav-light.png`（见 `config.mts` themeConfig.logo） |
| `/img/ref/*` 等其余 | 5 | 其中 `hero-magnet-sensor-render.png` 只在 `config.mts` 的 og:image 里以字符串拼出（`base + 'img/ref/hero-magnet-sensor-render.png'`），md 里搜不到——**这一个是误报，别删**；首页 hero 用的是同名 `.webp` |

**建议**：不要在 render.py 里改，这是资源目录治理问题。做法是给 `scripts/images.py` 加一个 `--prune` 模式：以「渲染完成后的 `docs/**/*.md` 全文 + `config.mts`」为引用集，把不在引用集里的 `public/images/**`、`public/img/hero|prod|cat/**` 列出来供人工确认后删除。**`config.mts` 必须一起扫**，否则会误删 og:image。

---

## 3. 孤岛页面：0

从首页 `/msite/` + nav + 两个 sidebar 出发做可达性闭包，195 篇全部可达。
25 篇应用案例页**不在** `/applications/` 的 sidebar 里（该 sidebar 只有 5 条：总览 + 4 个领域），但都由对应领域页的卡片链到，所以不算孤岛。若希望案例页在左侧目录里可见，需要在 render.py 生成 sidebar 的部分给每个领域加 `items`。

---

## 4. sidebar / nav

- nav 33 条、products sidebar 159 条、applications sidebar 5 条，**全部解析得到存在的页面，dist 里也都有 html**，没有指向被裁页面的条目。
- products sidebar 内部**无重复**；nav 里的产品链接全部是 products sidebar 的子集（系列页在 nav 下拉与左侧目录各出现一次，是 VitePress 常规，不算重复）。
- 全部 159 个产品页（19 系列 + 134 型号 + 5 产品线 + 产品中心）**都在 sidebar 里出现**，无遗漏。
- `/about/` 在 nav 里出现 4 次（`/about/#公司简介`、`#核心价值观`、`#品质认证`、`#加入我们`），是同一页的四个锚点，四个 id 在 `dist/about/index.html` 里都存在，属设计使然。
- ⚠️ **唯一的真问题**：`KTH4603AA-STx` / `KTH4603AB-STx` 在 sidebar 里各出现两次，一次挂在 `/products/switch/kth460/`、一次挂在 `/products/switch/kth462/`——同一个型号两个 URL。见第 6、7 节。

---

## 5. 锚点：全部有效

全站 141 条页内锚点链接，全是型号页 / 系列页的 `<a href="#技术文档">`。逐条比对 dist 里该页真实的 heading id（`id="技术文档"`），**0 条落空**。
render.py 里这条链接与「有没有 docs」是绑定的（`render_model_pages` 约 987 行：有 docs 才输出 `href="#技术文档"`，没有就输出 `href="/contact"`），逻辑本身是对的，所以没出现「链到不存在的章节」。

---

## 6. 跨系列污染：KTH460 与 KTH462 被 4 字符前缀糊在一起

**症状**

| 文件 | 证据 |
|---|---|
| `docs/products/switch/kth462/kth4603aa-stx.md` | KTH4603 属于 **KTH460 系列**（微功耗 3D 霍尔开关），却生成在 `kth462/`（超灵敏 2D 霍尔开关）下面；面包屑、kicker、lead 全部写成「KTH462 系列超灵敏 2D 霍尔开关」 |
| `docs/products/switch/kth462/kth4603ab-stx.md` | 同上 |
| `docs/products/switch/kth460.md` | 规格表表头 `KTH4603AA-STx` / `KTH4603AB-STx` 的链接指向 `/msite/products/switch/kth462`（**别的系列页**），而不是自家的 `/products/switch/kth460/kth4603aa-stx` |

**根因**：`series_prefixes()`（render.py 约 717 行）用 `re.findall(r'KT[A-Z]\d{2}', t)` 只取**两位数字**，于是 `KTH460 系列` 和 `KTH462 系列` 的前缀都是 `KTH46`。`_family_map()` 用 `setdefault` 建表，`KTH46` 只能归一个主人，于是：

- `owner_of('KTH4603AA-STx')` 返回 `kth462`；
- `model_link('kth460', 'KTH4603AA-STx')` 走进「别系列型号 → 链到它自己的系列页」分支，吐出 `/products/switch/kth462`；
- `render_model_pages('kth462', …)` 里 `series_prefix('KTH4603AA-STx') == 'KTH46'` 恰好落在 `own_all = {'KTH46'}` 里，于是**没有被跳过**，照样在 kth462 下生成了页面。

**render.py 修法**：把前缀匹配从固定两位改成「贪吃到数字结束」，并按最长前缀择主：

```python
out = re.findall(r'KT[A-Z]\d{2,}', t)          # 717 行附近，\d{2} -> \d{2,}
```

同时 `_family_map()` 建表后，`owner_of()` 应当**按最长匹配前缀**查（先试 `KTH4603` 的 7 位、再 5 位、再 4 位），而不是拿 `series_prefix()` 的第一个结果去 dict 里点名。改完 `KTH460`/`KTH462` 就分得开；`kth16` 的 `KTH13/16/17 系列` 是多前缀写法，`series_prefixes` 的 `head` 分支已覆盖，改成 `\d{2,}` 后要确认 `head` 那条正则（`(\d{2})((?:\s*/\s*\d{2})+)`）同步放宽，否则 `KTH13/16/17` 会解析不出。

**已核对不是问题的**：`docs/products/switch/kth16/` 下的 17 个 `KTH17xx`、`KTH1722CC`、`KTH1731PU`，因为该系列本身叫「KTH13/16/17 系列」，目录 slug 是 `kth16` 但覆盖三个前缀，表头链接也都落在自家目录，**不算污染**。

---

## 7. 重复内容

- **正文完全相同的页面：0。**
- **同一个型号被渲染成两份**（真问题，第 6 节的直接后果）：

  | A | B | 差异 |
  |---|---|---|
  | `docs/products/switch/kth460/kth4603aa-stx.md`（5220 B） | `docs/products/switch/kth462/kth4603aa-stx.md`（4656 B） | 只差系列身份（KTH460 微功耗 3D vs KTH462 超灵敏 2D）与「技术文档」整节——**kth462 那份没有技术文档节**（`doc_matches` 在 kth462 的 docs 里匹配不到 KTH4603），参数表逐格相同 |
  | `docs/products/switch/kth460/kth4603ab-stx.md` | `docs/products/switch/kth462/kth4603ab-stx.md` | 同上 |

  `kth462` 那两份是多余的、且系列描述是错的，应随第 6 节的修复一并消失。修好前它们还会被 sidebar 各索引一次（第 4 节）。

- **同系列型号变体的近似页（516 对，ratio 0.985~0.9986）**：集中在 `ktm13`（457 对）、`kth16`（27）、`linear-hall`（13）、`kth78`（11）、`kth31`（4）、`kth25`（2）、`kth71`（1）。逐对看过 diff，差异都是真参数（磁感应阈值 `45 → 9`、封装 `QN16 → SOP8`、`CRC 是/否`、噪声 `0.015° → 0.004°`），**不是模板重复**。`render_model_pages` 里那段「摘要重复时逐步多带一个差异项直到本系列内唯一」的逻辑已经在防这件事，工作正常。

  这批页面本身没坏，但对 SEO 是薄内容风险（例如 `ktm1302sa` 与 `ktm1302sd` 相似度 0.9986，全文只差一个磁阈值数字）。若要处理，方向是在 render.py 里给差异字段加显性对比说明、或把差异过小的型号合并成一页多档位，**不属于本次链接巡检的结论**，只做提示。

---

## 8. 复现命令

```bash
# 链接 / 资源 / 孤岛 / sidebar / 锚点 / 重复
python scripts/qa_links.py        # 尚未落地；本次用临时脚本跑，逻辑见上文各节判据
```

本次巡检脚本为一次性产物，未写入仓库。若要常态化，建议把它落成 `scripts/qa_links.py` 并在 `render.py` 末尾调用一次，把第 1、4、6 节三类问题做成非零退出码——这三类都是**能被机器判死**的，靠人肉复查必然漏。
