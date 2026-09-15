# conntek-vitepress

把 www.conntek.com.cn 的中文站整理成 Markdown，用 VitePress 本地渲染。

## 本地查看

```bash
npm install
npm run docs:dev      # http://localhost:5173
npm run docs:build && npm run docs:preview
```

## 目录

| 路径 | 内容 |
|---|---|
| `docs/index.md` | 首页（企业宣传视频、热门产品） |
| `docs/products/` | 产品中心：总览 + 5 个类目 + 20 个产品详情页（规格参数、技术文档、视频） |
| `docs/applications/` | 市场应用：总览 + 4 个场景 |
| `docs/services.md` | 磁仿真&技术服务 |
| `docs/tech-talks.md` | 技术洞见（16 篇，链接指向公众号原文） |
| `docs/about/` | 公司介绍、核心价值观、品质认证、加入我们 |
| `docs/contact.md` | 联系方式与办公地点 |
| `docs/public/images` | 内容图片（产品图、感应方向图、应用图、案例图等） |
| `docs/public/videos` | 官网视频 |
| `docs/public/files` | 技术文档 PDF 与上位机安装包，来自官网免登录下载接口 |
| `cache/` | 抓取下来的原始 HTML（`index.json` 为 URL → 文件映射）、`assets.json` 资源清单 |
| `scripts/crawl.py` | 从首页广度遍历全站页面，写入 `cache/` |
| `scripts/build.py` | 从 `cache/` 生成 `docs/`；加 `--download` 下载图片/视频/文件 |

## 重新同步官网

```bash
npm run fetch   # 重新抓取 + 生成 + 增量下载资源（已存在的文件跳过）
```

md 文件由 `scripts/build.py` 生成，**直接改 md 会在下次生成时被覆盖**，排版调整请改脚本或 `docs/.vitepress/theme/style.css`。

## 与原站的对应关系

- 原站 5 个类目 URL 其实是同一页面切 tab，这里拆成 5 个类目页；`57xilie` 与 `magneticAngleEncoderChip` 是同一产品（KTH57），合并为 `/products/3d-hall/kth57`。
- `linearHallChip`（线性霍尔芯片）不在官网产品总览里，是旧页面，保留在「开关芯片」下并标注旧版。
- 技术洞见原站分 3 页，这里合成一页按年份分组。
- 装饰性图标（导航、hover 图、地址/邮件小图标）未收录。
- 页面上不展示原网页链接。
- `KTH1362 Series产品手册.pdf` 官网下载接口返回 500，页面上标注「官网暂不可下载」。
- 图片用 `scripts/compress_images.py` 压缩过（>200KB 的图长边限 1400px、PNG 量化 256 色），重新下载后要再跑一次。
