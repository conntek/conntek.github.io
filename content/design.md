# Design reference: conntek.grosso.link

Extracted 2026-09-15 from the live CSS (`/assets/style.CKij4BgV.css`) and computed styles at 1440 px and 375 px.
Pages inspected: home, products overview, product series, product detail, applications, knowledge, knowledge article, blog.

**Key finding:** the reference is itself **VitePress 1.6.3 with the stock default theme**. It is *not* a bespoke design.
Its custom CSS is only ~1 KB: a 48 px logo, a wider hero image (760 px), a `.reference-link` style,
`sup` fix, and a GitHub icon button. Everything else (colors, type scale, cards, tables) is VitePress defaults
with the **indigo** brand scale. So "adopting its look" means: stay close to the default theme, keep the indigo brand,
use the big two-tone logo, a tall hero with a transparent product render on white, emoji-icon feature cards,
and plain doc pages with sidebar + outline. No gradients, no photos, no dark sections, no blur.

---

## Palette

Light mode (`:root`) and dark mode (`.dark`), exact values from CSS.

| Role | Token | Light | Dark |
|---|---|---|---|
| Brand 1 (links, active nav, hero name) | `--vp-c-brand-1` = indigo-1 | `#3451b2` | `#a8b1ff` |
| Brand 2 (hover) | `--vp-c-brand-2` | `#3a5ccc` | `#5c73e7` |
| Brand 3 (primary button bg) | `--vp-c-brand-3` | `#5672cd` | `#3e63dd` |
| Brand soft | `--vp-c-brand-soft` | `rgba(100,108,255,.14)` | `rgba(100,108,255,.16)` |
| Link hover (custom `.reference-link`) | – | `#1e40af` | – |
| Background | `--vp-c-bg` | `#ffffff` | `#1b1b1f` |
| Background alt (sidebar) | `--vp-c-bg-alt` | `#f6f6f7` | `#161618` |
| Background soft (cards, th, zebra rows) | `--vp-c-bg-soft` | `#f6f6f7` | `#202127` |
| Elevated (menus) | `--vp-c-bg-elv` | `#ffffff` | `#202127` |
| Border (switch, inputs) | `--vp-c-border` | `#c2c2c4` | `#3c3f44` |
| Divider / hairline | `--vp-c-divider` | `#e2e2e3` | `#2e2e32` |
| Text 1 | `--vp-c-text-1` | `#3c3c43` | `#dfdfd6` |
| Text 2 (lead, details, th) | `--vp-c-text-2` | `#67676c` | `#98989f` |
| Text 3 (meta) | `--vp-c-text-3` | `#929295` | `#6a6a71` |
| Gray 1/2/3 (alt button) | `--vp-c-gray-1/2/3` | `#dddde3` / `#e4e4e9` / `#ebebef` | `#515c67` / `#414853` / `#32363f` |
| Gray soft (icon tile, switch) | `--vp-c-gray-soft` | `rgba(142,150,170,.14)` | `rgba(101,117,133,.16)` |
| Tip/green | green-1/2/3 | `#18794e` `#299764` `#30a46c` | `#3dd68c` `#30a46c` `#298459` |
| Warning/yellow | yellow-1/2/3 | `#915930` `#946300` `#9f6a00` | `#f9b44e` `#da8b17` `#a46a0a` |
| Danger/red | red-1/2/3 | `#b8272c` `#d5393e` `#e0575b` | `#f66f81` `#f14158` `#b62a3c` |

**Colors present only in imagery (not in CSS)** — sampled from the logo and hero render:

| Where | Hex | Note |
|---|---|---|
| Logo "CO" red | `#c30d23` | brand wordmark red |
| Logo "NNTEK" dark teal | `#25414c` | brand wordmark teal-navy |
| Logo Chinese subline | `#333333` | |
| Hero magnet render red | `#f00000` → `#b00000` | cylindrical gradient on the magnet side |
| Hero magnet top gray / chip | `#707070`–`#808080`, `#3a3a30` | |

The site never uses the logo red/teal in UI; indigo is the only UI accent. Red appears only through the logo and the hero render, which gives the page its "blue UI + red product" contrast.

## Typography

Font stack: `"Punctuation SC", "Inter", ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"` (Inter woff2 self-hosted; CJK falls back to system: PingFang SC / Microsoft YaHei). Mono: `ui-monospace, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace`.

| Element | Size / line-height (desktop ≥960) | Mobile (375) | Weight | Letter-spacing | Color |
|---|---|---|---|---|---|
| Hero name (line 1, brand colored) | 56 / 64 px | 32 / 40 px, centered | 700 | -0.4px | brand-1 |
| Hero text (line 2) | 56 / 64 px, max-width 576 | 32 / 40 px | 700 | -0.4px | text-1 |
| Hero tagline | 24 / 36 px | 18 / 28 px | 500 | 0 | text-2 |
| Doc h1 | 32 / 40 px | 28 / 40 px | 600 | -0.64px (-0.02em) | text-1 |
| Doc h2 | 24 / 32 px; margin-top 48, padding-top 24, border-top 1px divider | same | 600 | -0.48px | text-1 |
| Doc h3 | 20 / 28 px; margin-top 32 | same | 600 | -0.2px | text-1 |
| Body p | 16 / 28 px; margin 16px 0 | same | 400 | 0 | text-1 |
| List item | 16 / 24 px; ul padding-left 20 | same | 400 | 0 | text-1 |
| Strong | inherit | | 600 | | text-1 |
| Feature title | 16 / 24 px | same | 600 | | text-1 |
| Feature details | 14 / 24 px | same | 500 | | text-2 |
| Nav link | 14 px, line-height 64 | – | 500 | | text-1; active brand-1 |
| Sidebar group title | 14 / 24 px | | 700 | | text-1 |
| Sidebar link | 14 / 24 px | | 500 | | text-2; active brand-1 |
| Outline ("On this page") | title 14/32 600; links 14/32 400 | | | | text-2 |
| Table cell | 14 / 24 px | | th 600 | | th text-2 |
| Button | 14 px, line-height 38 | | 600 | | |

## Spacing & layout

- Nav height **64 px**; logo image **48 px** tall (40 px ≤768, 36 px ≤480).
- Home content max-width **1152 px**; side padding 64 px (≥960), 48 px (≥640), 24 px (mobile).
- Hero: `padding: 144px 64px 64px; margin-top: -64px` (sits under transparent nav) → ~80 px visible top space. Mobile `112px 24px 48px`.
- Hero image container width `min(100%, 760px)`; image to the right of text on desktop, above text on mobile.
- Feature grid: 4 columns at ≥960 (`grid-4`), 2 at ≥640, 1 on mobile; gutter 16 px (8 px item padding, -8 px row margin).
- Doc page: sidebar 272 px (`--vp-sidebar-width`) on `bg-alt`; content column max **688 px**; right outline 224 px; doc padding 32/48 px top.
- Section rhythm in docs: h2 = 48 px top margin + 24 px padding + hairline. Home bottom margin 96 px.
- Radii: cards / flyout menu **12 px**; pager links **8 px**; icon tile / menu links **6 px**; buttons **20 px** (pill, 40 px tall); switch 11 px; hero image bg 50%.
- Shadows (only on floating UI): `--vp-shadow-3: 0 12px 32px rgba(0,0,0,.1), 0 2px 6px rgba(0,0,0,.08)`. Cards have **no** shadow.
- Hairlines: `1px solid #e2e2e3` everywhere (h2 top, nav divider under content, footer top, table cells, hr).

## Components

### Top nav
Transparent bar over the hero on home; on doc pages the content area gets white bg + bottom divider (no blur). Logo left (large two-tone image, no text title), links right: plain links and flyout groups with chevron, then appearance switch and GitHub icon. Flyout: white panel, 1px divider border, 12 px radius, shadow-3, 12 px padding, items 14px/32px with 6 px radius hover bg.

```css
.VPNavBar{height:64px}
.VPNavBarTitle .VPImage{height:48px!important;width:auto!important}
.VPNavBarMenuLink{font-size:14px;font-weight:500;padding:0 12px;line-height:64px}
.VPFlyout .VPMenu{border:1px solid var(--vp-c-divider);border-radius:12px;padding:12px;box-shadow:var(--vp-shadow-3)}
```

### Hero
Two-column: left big 2-line headline (line 1 in brand indigo, line 2 dark), gray tagline, two pill buttons; right a transparent-PNG 3D render (red/gray diametric magnets with chips and axis arrows) on plain white. No background gradient, no glow (`--vp-home-hero-image-background-image: none`).

```css
:root{--vp-home-hero-name-color:var(--vp-c-brand-1);--vp-home-hero-name-background:transparent;--vp-home-hero-image-background-image:none}
.VPHero .image-container{width:min(100%,760px)!important}
.VPHero .image-src{width:100%!important;max-width:100%!important;height:auto!important;object-fit:contain!important}
```

### Section headers
No eyebrow/kicker. A section = h2 with a hairline above (often prefixed by an emoji in the source), optional one-paragraph lead in body text, then h3 subgroups. Title-case not applicable (CJK).

```css
.vp-doc h2{margin:48px 0 16px;padding-top:24px;border-top:1px solid var(--vp-c-divider);font-size:24px;line-height:32px;font-weight:600;letter-spacing:-.02em}
```

### Feature cards
Soft gray tile (`#f6f6f7`), 1px border same color, 12 px radius, 24 px padding; top a 48×48 icon tile (gray-soft bg, 6 px radius, emoji at 24 px), 20 px gap, then title 16/600 and details 14/500 text-2. Hover (when linked): border turns brand-1.

```css
.VPFeature{background:var(--vp-c-bg-soft);border:1px solid var(--vp-c-bg-soft);border-radius:12px;transition:border-color .25s}
.VPFeature.link:hover{border-color:var(--vp-c-brand-1)}
.VPFeature .box{padding:24px}
.VPFeature .icon{width:48px;height:48px;border-radius:6px;background:var(--vp-c-default-soft);font-size:24px;margin-bottom:20px}
```

### Key numbers / stats
No dedicated stat component. Numbers appear inline in feature details and bold list items ("**label**: value"). If a stat block is needed, keep it in the feature-card language (soft tile, 12 px radius, number 32/40 600 brand-1, label 14/500 text-2).

### Feature lists
Plain `ul` with 20 px indent, 24 px line-height, bold lead-in term then colon then value.

### Tables
Block-level, horizontally scrollable, collapsed borders, header on soft gray, zebra rows.

```css
.vp-doc table{display:block;border-collapse:collapse;margin:20px 0;overflow-x:auto}
.vp-doc th,.vp-doc td{border:1px solid var(--vp-c-divider);padding:8px 16px;font-size:14px;line-height:24px}
.vp-doc th{background:var(--vp-c-bg-soft);color:var(--vp-c-text-2);font-weight:600;text-align:left}
.vp-doc tr:nth-child(2n){background:var(--vp-c-bg-soft)}
```

### Buttons
Pill, 40 px tall, 0 20 px padding, 14/600. Primary: brand-3 bg `#5672cd`, white text, hover brand-2. Secondary ("alt"): gray-3 bg `#ebebef`, text-1, hover gray-2.

```css
.VPButton{border-radius:20px;padding:0 20px;line-height:38px;font-size:14px;font-weight:600;border:1px solid transparent}
.VPButton.brand{background:var(--vp-c-brand-3);color:#fff}.VPButton.brand:hover{background:var(--vp-c-brand-2)}
.VPButton.alt{background:var(--vp-c-default-3);color:var(--vp-c-text-1)}.VPButton.alt:hover{background:var(--vp-c-default-2)}
```

### Tags / badges
Not used on the pages seen; the default `VPBadge` (soft tinted bg, 12 px radius, 12/18 600) is the matching style.

### Links
Brand-1, weight 500, no underline; `.reference-link` hover `#1e40af` + underline. Superscript refs `sup{font-size:.75em;top:-.5em}`.

### Sidebar & outline (doc pages)
Sidebar full height on `#f6f6f7`, padding `64px 32px 96px`, group titles 14/700, links 14/500 text-2, active brand-1. Right outline "On this page" 14/600, links 14/400 text-2. Pager at bottom: bordered 8 px radius boxes.

### Footer
Minimal: 32 px padding, top hairline, white bg, centered small text. No multi-column footer.

### CTA blocks
None besides the hero buttons. Suggested in-language CTA: soft tile (bg-soft, 12 px radius, 32 px padding), h3 + text-2 lead + brand pill button.

## Imagery

- **Hero:** a single 3D-rendered technical illustration on transparent background (isometric diametric magnets in saturated red + gray, small dark sensor chips, thin gray axis arrows). Framed with no box, no crop, no shadow, `object-fit: contain`, up to 760 px wide.
- **Logo:** large raster wordmark (red + dark teal Latin, dark gray Chinese subline), shown at 48 px height — much taller than VitePress' default 24 px, which is a signature trait.
- **Icons:** emoji in gray tiles on feature cards and before h2 headings. No icon font, no SVG set.
- **No photos, no gradients, no textures, no background images, no product package renders in body pages.** Doc pages are text + tables only.

## Assets saved

Folder: `D:\VerySync\VerySync_works\conntek-vitepress\docs\public\img\ref\` (total ~250 KB)

| File | What it is | Suggested use |
|---|---|---|
| `hero-magnet-sensor-render.webp` (1088×964, alpha, 21 KB) | 3D render: three diametric magnets with chips and field/axis arrows, transparent | Home hero `image`; also decorative art on "technology" sections |
| `hero-magnet-sensor-render.png` (same, 39 KB) | PNG fallback of the above | Where webp alpha is not wanted |
| `logo-conntek.png` (1136×410, alpha, 122 KB) | Two-tone wordmark with Chinese subline, transparent | `themeConfig.logo`, shown at 48 px height |
| `logo-conntek.webp` (same, 68 KB) | webp of logo | Same, lighter |

Not saved: no other images exist on the site (feature icons are emoji; favicon request returns the HTML fallback).

## Recommended mapping to VitePress

These reproduce the reference exactly (it uses VitePress defaults, so most values equal the defaults; setting them explicitly guards against other overrides in `style.css`).

```css
:root{
  --vp-c-brand-1:#3451b2;
  --vp-c-brand-2:#3a5ccc;
  --vp-c-brand-3:#5672cd;
  --vp-c-brand-soft:rgba(100,108,255,.14);
  --vp-c-bg:#ffffff;
  --vp-c-bg-soft:#f6f6f7;
  --vp-c-bg-alt:#f6f6f7;
  --vp-c-bg-elv:#ffffff;
  --vp-c-divider:#e2e2e3;
  --vp-c-border:#c2c2c4;
  --vp-c-text-1:#3c3c43;
  --vp-c-text-2:#67676c;
  --vp-c-text-3:#929295;
  --vp-font-family-base:"Punctuation SC","Inter",ui-sans-serif,system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif,"Apple Color Emoji","Segoe UI Emoji";
  --vp-home-hero-name-color:var(--vp-c-brand-1);
  --vp-home-hero-name-background:transparent;
  --vp-home-hero-image-background-image:none;
  --vp-home-hero-image-filter:none;
  --vp-button-brand-bg:var(--vp-c-brand-3);
  --vp-button-brand-hover-bg:var(--vp-c-brand-2);
}
.dark{
  --vp-c-brand-1:#a8b1ff;
  --vp-c-brand-2:#5c73e7;
  --vp-c-brand-3:#3e63dd;
  --vp-c-brand-soft:rgba(100,108,255,.16);
  --vp-c-bg:#1b1b1f;
  --vp-c-bg-soft:#202127;
  --vp-c-bg-alt:#161618;
  --vp-c-bg-elv:#202127;
  --vp-c-divider:#2e2e32;
  --vp-c-border:#3c3f44;
  --vp-c-text-1:#dfdfd6;
  --vp-c-text-2:#98989f;
  --vp-c-text-3:#6a6a71;
}
.VPNavBarTitle .VPImage{height:48px!important;width:auto!important;max-height:48px!important}
@media (max-width:768px){.VPNavBarTitle .VPImage{height:40px!important}}
@media (max-width:480px){.VPNavBarTitle .VPImage{height:36px!important}}
.VPHero .image-container{width:min(100%,760px)!important}
.VPHero .image-src{width:100%!important;max-width:100%!important;height:auto!important;object-fit:contain!important}
```

Optional (not on the reference, but consistent with its logo): if a warmer brand tie-in is wanted, use the logo red `#c30d23` only for tiny accents (e.g. a 2 px underline on active nav or hero name second word) and the logo teal `#25414c` for footer text; keep indigo as the interactive color so links/buttons still match the reference.
