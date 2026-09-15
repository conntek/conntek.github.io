# conntek-vitepress

昆泰芯 CONNTEK 中文站内容的 VitePress 版本：所有页面按统一模板生成，发布在 GitHub Pages（`/msite/`）。

## 本地查看

```bash
npm install
npm run docs:dev        # http://localhost:5173/msite/
npm run docs:build && npm run docs:preview
```

## 生成流程

```
scripts/crawl.py       抓取原站页面            → cache/html/、cache/index.json
scripts/extract.py     抽取结构化内容          → cache/site.json、cache/assets.json
scripts/download.py    下载图片/视频/技术文档   → docs/public/{images,videos,files}
scripts/compress_images.py  压缩大图（文件名不变）
scripts/images.py      统一比例的派生图与图标   → docs/public/img/、cache/img_manifest.json
scripts/render.py      按模板渲染全部页面       → docs/**/*.md、docs/.vitepress/sidebar.json
```

常用：`npm run gen`（extract → images → render）。**md 由脚本生成，不要手改**，改文案改 `content/`，改版式改 `scripts/render.py` 与 `docs/.vitepress/theme/style.css`。

## 内容文件（content/）

| 文件 | 内容 |
|---|---|
| `copy.json` | 改写后的文案：栏目名、首页与各页导语、类目/应用描述、每个产品的型号名、导语、4 个关键参数、概述、核心特点、典型应用；`_notes` 记录修正与源数据冲突 |
| `specs.json` | 规范化的规格表（型号矩阵 / 参数对照），含合并列与示意图 |
| `figures.json` | 原站规格图片的判定：表格图已转写成文字表格，示意图保留，装饰图与挂错产品的图丢弃 |
| `conflicts.md` | **原站自相矛盾、需要确认的数据清单** |
| `icons-src/` | codex 生成的 28 张统一风格图标原图（产品 19、产品线 5、应用领域 4） |
| `design.md` | 视觉参考（conntek.grosso.link）的设计规格 |
| `qa_report*.md` | 监督检查报告 |

## 页面模板

所有内容页：面包屑（首页起）→ 眉题 → 标题 → 导语 → 关键数字 → 二级章节 → 行动区。

- 产品页：关键参数、下载按钮 → 产品概述 → 核心特点 → 规格参数（宽表可横向滑动、首列固定）→ 技术文档 → 视频资料 → 应用案例 → 同类产品
- 类目页：产品系列列表 → 应用案例 → 其他产品线
- 应用页：应用案例 → 推荐芯片一览 → 其他应用领域

## 发布

`.github/workflows/deploy.yml` 在推送到 `main` 时自动构建并发布到 GitHub Pages（`github-pages` 环境只允许 `main` 部署）：

```bash
git push github master:main
```

## 说明

- 页面上不展示原网页链接；技术洞见文章链接到微信公众号原文。
- `KTH1362 Series产品手册.pdf` 原站下载接口返回 500，页面标注「暂不可下载」。
- 视觉：扁平中性风格参考 conntek.grosso.link，强调色为 logo 红 #C30D23；首页主视觉取自该站的磁铁渲染图。
