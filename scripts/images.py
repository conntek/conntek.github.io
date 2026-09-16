"""生成统一比例的派生图片到 docs/public/img/，原图不动。

- 产品图：裁掉四周白边/透明边，按 4:3 等比居中放进透明画布（卡片、详情页头图统一视觉重量）
- 横幅/照片类封面：按固定比例居中裁剪（类目 2:1、技术洞见 16:9、办公地点 2:1、应用案例 1:1）
- logo：去白底生成透明 PNG，另出一版深色模式用（深灰字改白色，红色保留）
输出统一为 webp，质量 82。可重复运行。
"""
import json, os
from PIL import Image, ImageChops, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, 'docs', 'public')
OUT = os.path.join(PUB, 'img')
SITE = json.load(open(os.path.join(ROOT, 'cache', 'site.json'), encoding='utf-8'))
MANIFEST = {}


def load(p):
    im = Image.open(os.path.join(PUB, p.lstrip('/')))
    im.load()
    return im.convert('RGBA')


def trim(im, tol=18):
    """去掉接近白色或透明的边框。"""
    rgba = im.convert('RGBA')
    white = Image.new('RGBA', rgba.size, (255, 255, 255, 255))
    comp = Image.alpha_composite(white, rgba).convert('RGB')
    diff = ImageChops.difference(comp, Image.new('RGB', comp.size, (255, 255, 255)))
    diff = diff.convert('L').point(lambda v: 255 if v > tol else 0)
    box = diff.getbbox()
    return rgba.crop(box) if box else rgba


def fit(im, w, h, pad=0.08):
    """等比缩放后居中放进 w×h 透明画布，四周留 pad 比例的边。"""
    canvas = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    iw, ih = int(w * (1 - 2 * pad)), int(h * (1 - 2 * pad))
    im = im.copy()
    im.thumbnail((iw, ih), Image.LANCZOS)
    canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2), im)
    return canvas


def cover(im, w, h):
    return ImageOps.fit(im.convert('RGB'), (w, h), Image.LANCZOS, centering=(0.5, 0.5))


def save(im, name):
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, 'WEBP', quality=82, method=6)
    return '/img/' + name


def product_thumb(src, key, size=(800, 600)):
    if key in MANIFEST:
        return MANIFEST[key]
    MANIFEST[key] = save(fit(trim(load(src)), *size), key)
    return MANIFEST[key]


def logos():
    im = Image.open(os.path.join(PUB, 'images', 'logo.jpg')).convert('RGB')
    px = im.load()
    light = Image.new('RGBA', im.size)
    dark = Image.new('RGBA', im.size)
    lp, dp = light.load(), dark.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            # 与白色的距离作为不透明度，并反推去白底后的颜色
            a = 255 - min(r, g, b)
            if a < 12:
                lp[x, y] = dp[x, y] = (0, 0, 0, 0)
                continue
            k = 255 / a
            cr, cg, cb = [max(0, min(255, int(255 - (255 - c) * k))) for c in (r, g, b)]
            lp[x, y] = (cr, cg, cb, a)
            is_red = cr > 120 and cr > cg * 1.8
            dp[x, y] = (cr, cg, cb, a) if is_red else (236, 238, 242, a)
    box = light.getbbox()
    light, dark = light.crop(box), dark.crop(box)
    for name, img in (('logo-light.png', light), ('logo-dark.png', dark)):
        path = os.path.join(OUT, name)
        os.makedirs(OUT, exist_ok=True)
        img.save(path, optimize=True)
        MANIFEST[name] = '/img/' + name
    small = light.copy()
    small.thumbnail((360, 130), Image.LANCZOS)
    small.save(os.path.join(OUT, 'logo-nav-light.png'), optimize=True)
    small = dark.copy()
    small.thumbnail((360, 130), Image.LANCZOS)
    small.save(os.path.join(OUT, 'logo-nav-dark.png'), optimize=True)


def icons():
    """codex 生成的图标（content/icons-src/*.png）→ 去白底、裁边、统一放进 4:3 透明画布，输出 img/icons-web/*.webp。"""
    src_dir = os.path.join(ROOT, 'content', 'icons-src')
    if not os.path.isdir(src_dir):
        return 0
    n = 0
    for fn in sorted(os.listdir(src_dir)):
        if not fn.lower().endswith('.png'):
            continue
        im = Image.open(os.path.join(src_dir, fn)).convert('RGBA')
        # 生成器若给的是白底，把接近纯白的像素转成透明
        if im.getextrema()[3][0] == 255:
            px = im.load()
            for y in range(im.height):
                for x in range(im.width):
                    r, g, b, a = px[x, y]
                    m = min(r, g, b)
                    if m > 245:
                        px[x, y] = (r, g, b, 0)
                    elif m > 225:
                        px[x, y] = (r, g, b, int(255 * (255 - m) / 30))
        name = fn[:-4]
        MANIFEST['icon/' + name] = save(fit(trim(im, tol=8), 800, 600, pad=0.1), f'icons-web/{name}.webp')
        n += 1
    return n


def main():
    logos()
    print('icons', icons())
    for c in SITE['categories']:
        MANIFEST['cat/' + c['key']] = save(cover(load(c['cover']), 1000, 500), f'cat/{c["key"]}.webp')
        for i in c['items']:
            product_thumb(i['image'], f'prod/{i["slug"]}.webp')
    for slug, p in SITE['products'].items():
        if p['image']:
            MANIFEST[f'hero/{slug}'] = save(fit(trim(load(p['image'])), 1200, 900, pad=0.06), f'hero/{slug}.webp')
            MANIFEST[f'photo/{slug}'] = save(cover(trim(load(p['image'])), 1000, 750), f'photo/{slug}.webp')
    for a in SITE['applications']:
        for n, case in enumerate(a['cases']):
            MANIFEST[f'case/{a["key"]}/{n}'] = save(cover(load(case['image']), 600, 600), f'case/{a["key"]}-{n}.webp')
    for n, t in enumerate(SITE['techtalks']):
        MANIFEST[f'tt/{n}'] = save(cover(load(t['image']), 800, 450), f'tt/{n}.webp')
    for n, city in enumerate(SITE['contact']['cities']):
        MANIFEST[f'city/{n}'] = save(cover(load(city['image']), 800, 400), f'city/{n}.webp')
    for n, ph in enumerate(SITE['about']['photos']):
        im = load(ph)
        if min(im.size) >= 200:
            MANIFEST[f'about/{n}'] = save(cover(im, 1000, 625), f'about/{n}.webp')
    for n, c in enumerate(SITE['services']['cases']):
        MANIFEST[f'svc/{n}'] = save(fit(load(c), 800, 500, pad=0.03), f'svc/{n}.webp')
    v = SITE['home']['video']
    MANIFEST['poster/home'] = save(cover(load(v['poster']), 1280, 720), 'poster/home.webp')
    for slug, p in SITE['products'].items():
        for n, vid in enumerate(p['videos']):
            if vid['poster']:
                MANIFEST[f'poster/{slug}/{n}'] = save(cover(load(vid['poster']), 1280, 720), f'poster/{slug}-{n}.webp')
    json.dump(MANIFEST, open(os.path.join(ROOT, 'cache', 'img_manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
    print(f'{len(MANIFEST)} derived images, {total / 1048576:.1f} MB')


if __name__ == '__main__':
    main()
