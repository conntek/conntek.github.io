# QA 报告（第二轮，终审）：conntek-vitepress

- 审查日期：2026-09-15
- 对象：开发服务器 `http://127.0.0.1:5174/msite/` 的当前文件，以及 `content/copy.json`、`specs.json`、`figures.json`、`conflicts.md`、`scripts/render.py`、`docs/.vitepress/theme/style.css`、`docs/**/*.md`
- 方法：
  - 截图：用 `scripts/shot.py`（CDP 版）截了 12 个页面，每页三套（桌面 light、桌面 dark、`--mobile --light`），共 36 张。截图存放在 `C:/Users/wangc/AppData/Local/Temp/conntek-qa2/`，切片在 `t/` 子目录。shot.py 没有报横向溢出。
  - 事实核对：用脚本从 copy.json 的 `products` 中抽出全部数字和型号，逐个到 site.json 里同一产品的数据中查找；`home`、`pages`、`categories`、`applications` 四部分则到整份 site.json 中查找。另外把 19 个产品的 76 个 chip 逐个对到规格表的原始单元格。
  - 一致性：用脚本检查 34 个 md 页面的面包屑、kicker、H1、lead、stats、CTA 是否齐全、顺序是否正确，并与 sidebar.json 核对。
  - 链接：抽取 md 中全部 243 个站内 href/src（其中 `/files/` 80 个），全部用 HTTP 请求检查。由于 dev server 对不存在的路径也返回 200，另外逐个核对这些链接能否对应到 `docs/public` 下的文件或 md 文件。页内 `#锚点` 逐个核对是否有同名 H2。
- 本人只写了这份报告，没有改动其他文件。

## Summary

| 项 | 数量 |
|---|---|
| 第一轮 P0（4 条） | **已修复 4** |
| 第一轮 P1（22 条） | **已修复 17 / 部分修复 4 / 未修复 1** |
| 新发现 P0 | 0 |
| 新发现 P1 | 3 |
| 新发现 P2 | 13 |

**仍属 P0/P1、需要处理的项：**
- P1-19：移动端指标卡数值断行。这一轮还多出一个回归：hero 两个按钮的文字折成两行，溢出了胶囊形按钮。
- P1-7：移动端首页 hero，红色「昆泰芯微电子」仍然压在磁铁图上；H1 末尾「活」字单独成行。
- N-P1-1：移动端「产品概述」没有折叠成单列，正文被挤成约 130px 宽的窄条。
- N-P1-2：移动端内容区左右各留约 56px 边距，390px 宽的屏幕上正文只剩约 277px。
- N-P1-3：游戏手柄（KTH564X）在消费类电子页的「推荐芯片一览」里被标成「KTH57 系列」，KTH57 产品页的「应用案例」里也出现了游戏手柄。这与 copy 和 conflicts.md 已经定下的口径相矛盾。
- 部分修复但剩下的问题只到 P2 程度：P1-12、P1-16、P1-21（明细见下表）。

事实核对：copy.json 里**没有**找不到出处的数字或型号。唯一的例外是 kth16 的「15 系列」，它在 `_notes` 和 conflicts.md 里已经申报过。76 个 chip 全部能在规格表或 intro/highlights 里找到对应值；与源数据有冲突的几处，页面上显示的都是 conflicts.md 里记录的取值。

链接：渲染后的 md 里没有任何指向 conntek.com.cn 页面的链接，只有 `mailto:`。外链只有 19 个 `mp.weixin.qq.com`，都是技术文章。243 个站内链接全部能对应到实际文件，0 失效。页内锚点 0 失效，旋钮页的 `#技术文档` 按钮已经去掉。

---

## 第一轮问题逐条状态

| 编号 | 问题 | 状态 | 证据 |
|---|---|---|---|
| P0-1 | 分类页的「产品系列」列表崩坏 | 已修复 | `products/encoder/index.md:22` 已包进 `<div class="c-rows">`，每个产品是完整的 `a.c-row`（`c-row__media` 共 7 个、7 行）；截图 `encoder-light` / `encoder-dark` 横向行卡片正常 |
| P0-2 | KTH16 温度 | 已修复 | chip「温度（视型号）-40 ~ 85 / 125 ℃」；overview 第 1 段和 highlights「温度补偿」都按型号列出；`_notes` 已补申报；截图 `kth16-light_0` |
| P0-3 | 旋钮页空章节、死锚点 | 已修复 | `knob.md` 的 H2 只剩 产品概述 / 核心特点 / 产品形态 / 其他产品线；hero 按钮改为「索取产品资料」；全站 `href="#…"` 锚点核对 0 缺失 |
| P0-4 | 服务页图标在 light 模式下看不见 | 已修复 | 截图 `services-light_0`：三个红底圆形线稿图标清晰可见 |
| P1-1 | KTM52「在轴 / 轴向」 | 已修复（已申报） | name 改为中性的「21 位高精度 AMR 角度编码器」；overview 保留 intro 原话「采用轴向安装」；`_notes` 与 conflicts 已申报，并请站长确认 |
| P1-2 | 新增措辞 | 已修复 | 全站 md 里搜「稳零 / 电池供电 / 兼顾功耗 / 物理接触 / 成败」均为 0 处；consumer-electronics 的 desc 已改为逐个案例写明芯片 |
| P1-3 | μ 与 µ 混用 | 已修复 | 34 个 md 中 U+00B5 均为 0；specs.json 里的 4 处只出现在 `_changes` 说明文字里 |
| P1-4 | 「+125」 | 已修复 | 规格表和正文里已经没有。另有 3 处留在「原站参数图（文字版）」折叠区（kth57、kth78、ktax33），见 N-P2-4 |
| P1-5 | 关于页少一张照片 | 已修复（确认为非问题） | `company.png` 实际只有 40×38 px，是装饰小图，过滤掉是对的 |
| P1-6 | 图表与 HTML 数据冲突 | 已修复 | 冲突的图表文字版默认折叠，标题注明「与上表数据有出入，以产品手册为准」（`render.py:433`）；截图 `kth16-light_2`、`kth78-light_1` |
| P1-7 | 首页 hero 文字压图 | **部分修复** | 桌面端已修复（`home-light_0`：文字和图分开，标题一行显示完）。**移动端未修复**（`home-m-light_0`）：红色「昆泰芯微电子」叠在第三个磁铁图上，H1 折成「智能感知世界 传递美好生 / 活」 |
| P1-8 | 首页服务卡片带下划线 | 已修复 | `home-light_1` 中四张卡片没有下划线 |
| P1-9 | 首页 CTA 标题上方的横线 | 已修复 | style.css 的「行动区标题」规则已生效；`home-light_2` 中没有横线 |
| P1-10 | 宽表被截断 | 已修复 | 表格上方加了「↔ 表格较宽，可左右滑动查看全部参数」提示；`c-table--wide` 首列设为 sticky（style.css 约 1294–1308 行） |
| P1-11 | KTH78 合并单元格被展开 | 已修复 | `kth78-light_1`：等级、系列、校准、精度列都恢复了 rowspan |
| P1-12 | 图片风格和比例不统一 | **部分修复** | 产品卡、分类卡、应用卡统一换成了 `icons-web` 等轴测图标，首页、总览页、分类页已经统一。**残留**：旋钮页「产品概述」右侧只放了一张邮票大小的竖长海报缩略图（`knob-light_0`，移动端 `knob-m-light_0` 更明显），降为 P2 |
| P1-13 | 旋钮海报被压成缩略图 | 已修复 | 现在是两列、按原比例展示。副作用见 N-P2-6 |
| P1-14 | 技术分享页卡片局促 | 已修复 | `tech-light_0`：三列纵向卡片，标题 2 行、摘要 3 行 |
| P1-15 | 关于页排版 | 已修复 | 两张图叠放在右侧；第 3 张卡片标题为「RoHS / REACH」；`ktpz.png` 已移除；招聘表加了 `c-nowrap`，不再断行；「testpattern」那一句已移出列表（`about/index.md:84`）；CTA 主按钮为 `mailto:hr@` |
| P1-16 | 服务页排版 | **部分修复** | 「解决思路」的双重编号已去掉，改为横向 ①②③④ 小卡片；仿真案例的标题已删除。**残留**：三张仿真图仍只占卡片约 1/3（`services-light_1`），降为 P2 |
| P1-17 | 联系页邮箱溢出 | 已修复 | `.c-contact a, p { overflow-wrap:anywhere }`；`contact-light_0` 中 changhao.huang@ 在卡片内 |
| P1-18 | 章节导语多缩进 | 已修复 | style.css「章节导语与正文左对齐」；kth78、kth16、服务页的导语都与 H2 左对齐 |
| P1-19 | 移动端指标卡断行、按钮不齐 | **未修复（且有回归）** | `kth78-m-light_0`：「±0.35°（在 / 轴）」「120,000 / rpm」仍然折行；kth16 的「2.5 Hz ~ 40 / kHz」「-40 ~ 85 / / 125 ℃」也折行。**回归**：style.css 1379 行起的 `@media (max-width:480px) .c-actions .c-btn{flex:1}` 与 `.vp-doc a.c-btn{height:40px}` 叠加后，按钮被压窄，「下载技术 / 文档」「申请样品 / 咨 / 询」折成两行，文字溢出胶囊外框（kth78、kth16、knob 三页都能看到）。修复见下文 N-P1 小节 |
| P1-20 | 页面模式不统一 | 已修复（残留见 P2） | 34 页全部是「面包屑（首页起）→ kicker → H1 → lead → stats/chips → H2 → CTA」，脚本核对顺序 0 异常；contact 已有 CTA；无侧栏的页面与有侧栏的页面统一使用 `--c-page-width`。kicker 分三种写法，见 N-P2-1 |
| P1-21 | 栏目名不统一 | **部分修复** | 首页区块、面包屑、H1 已全部按 `section_names` 统一。**残留**：nav 顶层多了一个 section_names 里没有的分组名「服务与洞见」，而且「联系我们」挂在「关于昆泰」下面（sidebar.json nav），降为 P2 |
| P1-22 | 空章节规则 | 已修复 | 同类产品为空时改为「其他产品线」（knob、ktax33）；「应用案例」只在确有案例的 6 个产品页出现 |

---

## 新发现问题

### N-P1

**N-P1-1 移动端「产品概述」不折叠成单列（19 个产品页都受影响）**
- 证据：`kth78-m-light_0`、`kth16-m-light_0`、`knob-m-light_0` 中，正文被挤在左侧约 130px 宽，右侧是一张约 90px 的小图，一行只放得下 5 到 6 个字。
- 原因：`style.css:912` 的 `@media (max-width:860px){.c-split{grid-template-columns:1fr}}` 写在前面，而 `style.css:1325` 的 `.c-split--overview{grid-template-columns:minmax(0,1.4fr) minmax(0,1fr)}` 写在后面、优先级相同，于是把媒体查询覆盖掉了。
- 修复：在文件末尾追加 `@media (max-width:860px){.c-split--overview{grid-template-columns:1fr}}`，或者把 `.c-split--overview` 挪到 912 行的媒体查询之前。

**N-P1-2 移动端内容区左右边距约 56px，正文只剩约 277px 宽**
- 证据：所有带 `c-page` 的移动端截图，正文左边缘都在 x≈55/390 处。
- 原因：`style.css:71` 的 `.c-page .VPDoc .content{padding-left/right:32px !important}` 与 VitePress 自带的 `.VPDoc` 24px 内边距叠加在一起。这也是 P1-19 断行、按钮被压窄的主要诱因。
- 修复：`@media (max-width:640px){.c-page .VPDoc .content{padding-left:0 !important;padding-right:0 !important}}`（保留 VitePress 的 24px）。

**P1-19 的修复建议**（与 N-P1-2 一起做）：
- 按钮：`@media (max-width:480px){.c-actions .c-btn{flex:1 1 auto;white-space:nowrap}}`；或者保留 `flex:1`，把 `.vp-doc a.c-btn` 的 `height:40px` 改成 `min-height:40px`，并加 `padding-block:8px`。
- 指标卡：`@media (max-width:480px){.c-spec b{font-size:15px;white-space:nowrap}}`。另外把括注移到 label 里，例如 chip 值只写「±0.35°」，label 写「精度（在轴）」；「温度（视型号）」同理，值写「-40 ~ 125 ℃」、label 写「温度（最高，视型号）」。或者在 render.py 里，chip 值超过约 12 个字符时自动把括号内容移到 label。

**N-P1-3 游戏手柄（KTH564X）仍然显示为 KTH57 的产品和应用**
- 证据：
  - `docs/applications/consumer-electronics.md` 推荐芯片表：`<td class="c-mono">KTH564X</td><td><a href="/msite/products/3d-hall/kth57">KTH57 系列 三轴线性霍尔传感器</a></td><td>游戏手柄</td>`。截图 `consumer-light_0`。
  - 同一页的游戏手柄卡片链接指向 kth57。
  - `docs/products/3d-hall/kth57.md` 的「应用案例」里有 `<h3>游戏手柄</h3>`。
  - 同一页的 lead 却写着「游戏手柄采用 KTH564 系列」。conflicts.md 第 46 行定的口径是「游戏手柄列入 KTH564 系列的应用，不列入 KTH57」。页面上前后自相矛盾，而且显示的不是已经记录的取值。
- 原因：`render.py` 的 `render_applications()`（约 560–565 行）和 `related_cases()`（364 行）都直接使用 site.json 里案例的 `route`。
- 修复：在 render.py 里加一个芯片到页面的映射，`chip` 优先于 `route`：`CHIP_ROUTE={'KTH564X':'/products/switch/linear-hall', ...}`，在 `related_cases` 和推荐芯片表中都用 `CHIP_ROUTE.get(cse['chip'], cse['route'])`。修完之后 kth57 的案例里不再有游戏手柄，linear-hall 的案例里会多出这一条。站长确认前，也可以把这一行「对应产品」改成「KTH564 系列 线性霍尔芯片」。

### N-P2

1. **kicker 有三种写法**：总览类页面（产品中心、市场应用、服务、技术洞见、关于、联系）用「昆泰芯微电子」，分类页和应用子页用栏目名，产品页用型号。结构上说得通，但总览页的 kicker 与 H1 没有信息差。建议总览页改用英文栏目名或删掉 kicker。改动位置：render.py 的 `page_head()`。
2. **nav 结构**：顶层分组「服务与洞见」不在 `section_names` 里；「联系我们」挂在「关于昆泰」下。建议 nav 顶层直接用 `section_names` 的 6 个名字，或者把「服务与洞见」也加进 `section_names`。
3. **转速千分位写法不统一**：KTM52、KTM53 写「60000 rpm」，KTM58、KTM59、KTH78、KTH71 写「180,000 / 120,000 rpm」。同一个分类页上并排显示（`encoder-light_0`）。建议统一加千分位，改 copy.json 的 kth52、ktm53 以及 minispecs。
4. **「原站参数图（文字版）」没有做单位规范化**：还残留「-40 ~ +125 ℃」（kth57、kth78、ktax33），以及「40KHz」「2.25mA@1.8V」「-40℃~125℃」这类原始写法（kth16）。这部分是原图的逐字转录，可以接受；如果要与正文一致，在 render.py 输出 figure 文本时套用 specs 的同一套规范化函数即可。
5. **图片文件名带空格的问题未处理**（第一轮 P2-11）：`/images/Ultra-low power consumption and highly sensitive 3D Hall switch.png`、`/images/High-performance-low-power consumption-and-ultra-sensitive-2D-Hall-switch-direct.png`。目前能访问，部署前建议改成无空格的名字。
6. **旋钮页「产品形态」页面过长**：桌面端整页 12615px，海报占了约 9000px；两列按原比例排列，右列比左列长，最后一张单独落在右列，左侧留出大片空白（`knob-dark_6`）。建议用 `columns:2` 的瀑布流，或者限制每张海报的最大高度并支持点击放大。
7. **旋钮页概述图是邮票大小**（P1-12 残留）：建议 overview 改用 `kuntaikonb1` 的局部裁切图，或者去掉这张图。
8. **服务页「仿真案例」图片太小**（P1-16 残留），而且这个 H2 下面没有导语，与其他 H2 不一致。建议 `.c-fig--fill` 让图片铺满 16:10，并补一句导语（没有源数据可用就不加导语，但要保证全站规则一致）。
9. **CTA 版式不一致**：关于页、联系页的按钮排在右侧同一行，其他页面的按钮在文字下方（`about-light_1`、`contact-light_0`）。联系页 CTA 的「联系我们」按钮链接到页面自己。建议统一 CTA 版式，联系页去掉这个自链接按钮。
10. **移动端信息密度低**：stats 一行只放一个（`encoder-m-light_0`、`about-m-light_0`）；首页卡片单列排列，每张约 450px 高，首页移动端全长 13103px。建议 `@media (max-width:520px)` 下 `.c-stats` 用两列，产品/分类卡片改成横向小卡（图 96px + 文字）。
11. **侧栏长名称被截断**：设了 `nowrap` 和 `ellipsis`，但在截图里是直接截掉的，例如「KTM52 系列 21 位高精度 AMR 角度编」，看不到省略号。建议侧栏只显示型号，完整名称放进 `title`。
12. **案例卡的 kicker 含义不一致**：应用页上 kicker 是芯片名（KTM13xx、KTH564X），产品页「应用案例」里 kicker 是应用领域（消费类电子）。另外芯片名没有按 P2-3 统一：同时存在 `KTM13xx`、`KTH57xx`、`KTH564X`，而 desc 里写的是「KTM13 系列」。建议 render 时做一次芯片名规范化。
13. **消费类等应用页的「推荐芯片一览」在移动端很挤**：「对应产品」列折成 4 行（`consumer-m-light_2`）。建议这张表在移动端只显示「芯片 / 应用场景」两列，或者加 `c-table--wide` 和滑动提示。

### 顺带确认（不算问题）
- dark 模式下，照片类图片（感应方向图、概述图）用的是白底框，这是有意为之，与原图的白底一致。
- 技术洞见的 16 篇文章链到 `mp.weixin.qq.com`；联系页公开了销售的个人邮箱和手机号；招聘信息是 2021 年的。这几条在第一轮已列为标准问题，conflicts.md 第 56 行也已交站长确认。

---

## 事实核对明细

- **产品（19 个）**：copy.json 里 `products.*` 的全部数字和型号都能在 site.json 同一产品的 intro/highlights/specs/title 中找到。唯一找不到的是 kth16 的「15」（「系列包含 136、15、16、17 系列」），已在 `_notes` 和 conflicts 中申报。
- **chip（76 个）** 逐个对到原始单元格，下面是抽查到的规格表来源值：
  - KTM58：±0.02° 和 180,000 rpm（规格表）
  - KTM59：「在轴±0.02° / 离轴±0.05°」
  - KTH57：16Bit、1000Hz、2.8V~5.5V
  - KTO95：6 对模拟差分对输出、32-pin optoQFN、4.1-5.5V
  - KTM13：160nA@3V、5000Hz
  - KTH25：2.7mA、30KHz
  - KTM28：70μA
  - KTH31：1.00~8.90mV/GS(@3.3V)
  - KTAx333：1.8V-5.5V、30μA
  - KTH564：2.8-6.0V、3.3mA@5V、1.5~13mV/Gs
  - KTH16：2.5Hz（KTH1362SA）~ 40KHz
  - 结论：全部一致。
- **页面（home/pages/categories/applications）**：数字和型号 0 处找不到出处，包括「10余项」「5 大产品线」「2016」「电钻 / 电摩 / 无人机」等。
- **已申报冲突的页面取值与 conflicts.md 一致**：kth16 电压 1.7 ~ 5.5 V、kth25 2.7 ~ 32 V、ktm28 3 ~ 30 V、kth462 32.3 μA、kth460 2.5 ~ 5.5 V、ktm52 ±0.015°、kto95 取模拟电压 4.1 ~ 5.5 V、kth78 温度沿用 intro。
- **不一致**：只有 N-P1-3（游戏手柄）。

## 标准问题（第二轮）
1. dev server 对任何路径都返回 200，所以「用 curl 检查链接」这一项本身查不出死链。本轮改用「链接是否对应到 public 文件或 md 文件」来判断。建议把这个核对写进 render.py 的自检，或者用 `vitepress build` 的 dead link 检查。
2. `shot.py` 的整页截图里，fixed 定位的侧栏只出现在第一屏，下方是空白。这是截图方式造成的，页面本身没有这个问题，不应算作视觉缺陷。
