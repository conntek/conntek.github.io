"""生成统一比例的派生图片到 docs/public/img/，原图不动。

站点已固定深色（页面 #1b1b1f，卡片媒体面板 #202127），派生规则按"在深底上要好看且成套"来定：

- 先判底：四周一圈像素决定原图是 **浅底**、**深底** 还是 **实拍/混合**。
- 深底 → 连通抠底（只抠与边框连通的那片黑，不会把主体内部的黑吃掉）成透明，
  主体过暗时做一次伽马提亮，让它在 #202127 上还看得见。
- 浅底 → 不抠（抠了线稿黑字会在深底上消失、白色主体也会被吃掉），
  改为**整幅铺满浅色底板**，主体按统一留白居中：卡片上呈现为一块干净的浅色板，
  而不是原来那种四周透明、中间一坨白的"白板块"。
- 实拍/混合 → 居中裁剪铺满；但源图比例与目标差太多时改用底板留白，避免把图表文字裁掉。
- 主体一律按统一留白缩放，允许有限放大（UPSCALE_MAX），修掉原来 thumbnail 只缩不放
  导致小图在大画布里只占一小块的问题。

输出统一 webp，质量 82。可重复运行。低分辨率（需要放大才能铺满）的原图会在结尾列出。
"""
import json, math, os
import numpy as np
from PIL import Image, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, 'docs', 'public')
OUT = os.path.join(PUB, 'img')
SITE = json.load(open(os.path.join(ROOT, 'cache', 'site.json'), encoding='utf-8'))
MANIFEST = {}

PANEL = (0x20, 0x21, 0x27)      # 卡片媒体面板色，仅用于判读，不写进图里
PLATE = (0xf2, 0xf3, 0xf6)      # 浅底图统一用的底板色
UPSCALE_MAX = 2.6               # 允许的最大放大倍数，超过就不再放大（宁可小也不糊）
LOWRES = []                     # (key, 原图, 需要的放大倍数)


# ---------------------------------------------------------------- 基础工具

def load(p):
    im = Image.open(os.path.join(PUB, p.lstrip('/')))
    im.load()
    return im.convert('RGBA')


def arr(im):
    return np.asarray(im.convert('RGBA'), dtype=np.uint8)


def luma(rgb):
    return rgb[..., 0] * 0.299 + rgb[..., 1] * 0.587 + rgb[..., 2] * 0.114


def ring(a, k=2):
    """四周一圈像素。"""
    return np.concatenate([a[:k].reshape(-1, a.shape[-1]), a[-k:].reshape(-1, a.shape[-1]),
                           a[:, :k].reshape(-1, a.shape[-1]), a[:, -k:].reshape(-1, a.shape[-1])])


def classify(im):
    """返回 'light' / 'dark' / 'photo'。"""
    a = arr(im)
    if (a[..., 3] < 16).mean() > 0.04:       # 原图自带透明底
        return 'alpha'
    r = ring(a)
    rgb = r[:, :3].astype(np.int16)
    if (rgb.min(axis=1) >= 234).mean() > 0.88:
        return 'light'
    if (rgb.max(axis=1) <= 30).mean() > 0.88:
        return 'dark'
    return 'photo'


def connected_bg(mask, max_dim=192):
    """mask 里与边框连通的那部分（缩小后做泛洪，再放大回去，够用且快）。"""
    h, w = mask.shape
    s = max(1, int(math.ceil(max(h, w) / max_dim)))
    small = np.asarray(Image.fromarray((mask * 255).astype(np.uint8)).resize(
        (max(1, w // s), max(1, h // s)), Image.BILINEAR)) > 100
    reach = np.zeros_like(small)
    reach[0], reach[-1], reach[:, 0], reach[:, -1] = small[0], small[-1], small[:, 0], small[:, -1]
    for _ in range(small.shape[0] + small.shape[1]):
        nxt = reach.copy()
        nxt[1:] |= reach[:-1]
        nxt[:-1] |= reach[1:]
        nxt[:, 1:] |= reach[:, :-1]
        nxt[:, :-1] |= reach[:, 1:]
        nxt &= small
        if np.array_equal(nxt, reach):
            break
        reach = nxt
    big = np.asarray(Image.fromarray((reach * 255).astype(np.uint8)).resize(
        (w, h), Image.BILINEAR)) > 40
    return mask & big


def dekey(im, dark, tol=38):
    """抠掉与边框连通的平涂背景。

    背景色取四周一圈的中位数（而不是写死纯黑/纯白），这样带噪点的灰底、米白底也抠得干净；
    离背景色越远越不透明，边缘自然过渡。浅底还要去掉白色预乘，否则主体边上留一圈灰白。
    """
    a = arr(im).astype(np.int16)
    bgc = np.median(ring(a)[:, :3], axis=0)
    dist = np.abs(a[..., :3] - bgc).max(axis=2)
    soft = np.clip(dist * 255 // tol, 0, 255)
    soft[soft < 120] = 0          # 背景里的噪点/压缩振铃不要留成半透明黑渣，直接清零
    bg = connected_bg(dist < tol)
    alpha = a[..., 3].copy()
    alpha[bg] = np.minimum(alpha[bg], soft[bg])
    if not dark:
        edge = bg & (soft > 0)
        if edge.any():
            k = 255.0 / np.maximum(soft[edge], 1)
            for c in range(3):
                a[..., c][edge] = np.clip(255 - (255 - a[..., c][edge]) * k, 0, 255)
    a[..., 3] = alpha
    return Image.fromarray(a.astype(np.uint8), 'RGBA')


def transparent_ratio(im):
    return float((arr(im)[..., 3] < 32).mean())


def alpha_trim(im, tol=8):
    """按可见像素（含浅底判定）裁到主体外接框。"""
    a = arr(im)
    if (a[..., 3] < 200).mean() > 0.02:
        vis = a[..., 3] > 16
    else:
        white = Image.new('RGBA', im.size, (255, 255, 255, 255))
        comp = np.asarray(Image.alpha_composite(white, im).convert('RGB'), dtype=np.int16)
        vis = (255 - comp).max(axis=2) > tol
    ys, xs = np.where(vis)
    if not len(ys):
        return im
    return im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))


def lift_dark(im, target=112):
    """主体整体偏暗时做一次伽马提亮，保证在 #202127 上能看见。"""
    a = arr(im)
    vis = a[..., 3] > 128
    if vis.sum() < 64:
        return im
    l = luma(a[..., :3].astype(np.float32))[vis]
    med = float(np.median(l))
    if med >= target - 12 or med < 3:
        return im
    g = max(0.42, math.log(target / 255.0) / math.log(med / 255.0))
    lut = (np.clip((np.arange(256) / 255.0) ** g, 0, 1) * 255).astype(np.uint8)
    out = a.copy()
    out[..., :3] = lut[a[..., :3]]
    return Image.fromarray(out, 'RGBA')


def scale_to(im, iw, ih, key=None, src=None):
    """等比缩放到 iw×ih 内，允许有限放大；需要放大过多的记进 LOWRES。"""
    k = min(iw / im.width, ih / im.height)
    if k > 1:
        if key and k > 1.15:
            LOWRES.append((key, src, round(k, 2)))
        k = min(k, UPSCALE_MAX)
    w, h = max(1, round(im.width * k)), max(1, round(im.height * k))
    return im.resize((w, h), Image.LANCZOS)


def place(im, w, h, pad=0.07, plate=None, key=None, src=None):
    """主体按统一留白居中放进 w×h；plate 给定则铺满不透明底板，否则透明。"""
    canvas = Image.new('RGBA', (w, h), (plate + (255,)) if plate else (255, 255, 255, 0))
    im = scale_to(im, int(w * (1 - 2 * pad)), int(h * (1 - 2 * pad)), key, src)
    canvas.paste(im, ((w - im.width) // 2, (h - im.height) // 2), im)
    return canvas


def cover(im, w, h, centering=(0.5, 0.5)):
    return ImageOps.fit(im.convert('RGB'), (w, h), Image.LANCZOS, centering=centering).convert('RGBA')


def focus(im):
    """实拍图的裁剪中心：按"离全图均值最远"的像素质心，避免把主体裁到边上。"""
    a = np.asarray(im.convert('RGB').resize((96, 96), Image.BILINEAR), dtype=np.float32)
    d = np.abs(a - a.mean(axis=(0, 1))).sum(axis=2)
    d = np.clip(d - np.percentile(d, 60), 0, None)
    if d.sum() < 1e-3:
        return (0.5, 0.5)
    ys, xs = np.mgrid[0:96, 0:96]
    cx, cy = float((xs * d).sum() / d.sum()) / 95, float((ys * d).sum() / d.sum()) / 95
    return (min(0.78, max(0.22, cx)), min(0.78, max(0.22, cy)))


def is_lineart(im, min_share=0.15, min_thin=0.72, k=5):
    """主体是不是"细的深色笔画"（黑字、细线、标注）——这种放到深底上会直接消失。

    判据：深色像素被 5×5 腐蚀后还剩多少。成块的深色主体（方向盘、黑面板）留得下来，
    字和细线留不下来；留不下来的那部分占比高，就必须垫浅色底板。
    """
    a = arr(im)
    vis = a[..., 3] > 128
    dark = vis & (luma(a[..., :3].astype(np.float32)) < 92)
    n = int(dark.sum())
    if n < max(64, min_share * max(1, vis.sum())):
        return False
    er = np.asarray(Image.fromarray((dark * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(k))) > 127
    return (1 - er.sum() / n) > min_thin


def isolate(src, w, h):
    """第一步：把主体从原底上摘出来。返回 (主体图, 倾向底色 'dark'/'light'/None=实拍)。

    实拍图不摘，直接按比例判定裁剪或垫底板；渲染图按底色抠成透明并裁到主体外接框。
    深底图若几乎没抠掉东西，说明那不是平涂背景而是暗调实拍，按实拍走。
    """
    im = load(src)
    kind = classify(im)
    if kind == 'dark':
        cut = dekey(im, dark=True)
        if transparent_ratio(cut) < 0.12:
            kind = 'photo'
        else:
            return alpha_trim(cut, tol=6), 'dark'
    if kind == 'light':
        cut = dekey(im, dark=False)
        if transparent_ratio(cut) < 0.12:
            kind = 'photo'
        else:
            return alpha_trim(cut, tol=6), 'light'
    if kind == 'alpha':
        return alpha_trim(im), 'dark'
    ar = (im.width / im.height) / (w / h)
    # 比目标宽的实拍可以放心裁（裁的是两侧留白）；比目标高的多是竖版图文，裁了会掉字
    # 竖版图文（海报、带文字的实拍）裁了就掉字，判到就不裁
    if ar < 0.62 or ar > 2.6 or (ar < 0.9 and is_lineart(im, 0.04, 0.40)):
        return im, 'wide'
    return im, None


def render(sub, pref, w, h, pad, backdrop, key=None, src=None):
    """第二步：按本组统一的底（透明或浅色底板）落版。"""
    if pref is None:
        return cover(sub, w, h, focus(sub))
    if pref == 'wide':                       # 长条/竖版：不裁，按本组的底留白
        return place(sub, w, h, pad=0.04, plate=PLATE if backdrop == 'plate' else None, key=key, src=src)
    if backdrop == 'plate' or is_lineart(sub):
        return place(sub, w, h, pad=pad, plate=PLATE, key=key, src=src)
    return place(lift_dark(sub), w, h, pad=pad, key=key, src=src)


def batch(srcs, w, h, pad=0.07, keys=None):
    """一组卡片一起决定底色：少数服从多数，保证同一栅格里看着是一套。"""
    keys = keys or [None] * len(srcs)
    subs = [isolate(s, w, h) for s in srcs]
    prefs = [p for _, p in subs if p in ('dark', 'light')]
    backdrop = 'plate' if prefs.count('light') > prefs.count('dark') else 'clear'
    return [render(sub, pref, w, h, pad, backdrop, k, s)
            for (sub, pref), k, s in zip(subs, keys, srcs)]


def save(im, name):
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, 'WEBP', quality=82, method=6)
    return '/img/' + name


# ---------------------------------------------------------------- logo / 图标

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
    """codex 生成的图标（content/icons-src/*.png）→ 去白底、裁边、统一放进 4:3 透明画布。"""
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
            a = arr(im).astype(np.int16)
            m = a[..., :3].min(axis=2)
            soft = np.clip((255 - m) * 255 // 30, 0, 255)
            a[..., 3] = np.where(m > 225, np.minimum(a[..., 3], soft), a[..., 3])
            im = Image.fromarray(a.astype(np.uint8), 'RGBA')
        name = fn[:-4]
        # 图标是给深底用的白/红线稿，只对整体过暗的做一点提亮
        MANIFEST['icon/' + name] = save(place(lift_dark(alpha_trim(im), target=104), 800, 600, pad=0.09),
                                        f'icons-web/{name}.webp')
        n += 1
    return n


# ---------------------------------------------------------------- 主流程

def main():
    logos()
    print('icons', icons())
    for c in SITE['categories']:
        im = load(c['cover'])
        MANIFEST['cat/' + c['key']] = save(cover(im, 1000, 500, focus(im)), f'cat/{c["key"]}.webp')
    # 产品图：卡片缩略用类目里那张，详情页头图/正文配图用产品自己那张，各自成批定底色
    cards = {}
    for c in SITE['categories']:
        for i in c['items']:
            cards.setdefault(i['slug'], i['image'])
    cs = list(cards.items())
    for (slug, _), im in zip(cs, batch([s for _, s in cs], 800, 600, 0.07, [f'prod/{k}.webp' for k, _ in cs])):
        MANIFEST[f'prod/{slug}.webp'] = save(im, f'prod/{slug}.webp')
    items = [(s, p['image']) for s, p in SITE['products'].items() if p['image']]
    srcs = [src for _, src in items]
    for (slug, _), im in zip(items, batch(srcs, 1200, 900, 0.05, [f'hero/{s}' for s, _ in items])):
        MANIFEST[f'hero/{slug}'] = save(im, f'hero/{slug}.webp')
    for (slug, _), im in zip(items, batch(srcs, 1000, 750, 0.04)):
        MANIFEST[f'photo/{slug}'] = save(im, f'photo/{slug}.webp')
    cases = [(a['key'], n, c['image']) for a in SITE['applications'] for n, c in enumerate(a['cases'])]
    ckeys = [f'case/{k}/{n}' for k, n, _ in cases]
    for (k, n, _), im in zip(cases, batch([s for _, _, s in cases], 800, 600, 0.06, ckeys)):
        MANIFEST[f'case/{k}/{n}'] = save(im, f'case/{k}-{n}.webp')
    tts = [t['image'] for t in SITE['techtalks']]
    for n, im in enumerate(batch(tts, 800, 450, 0.03, [f'tt/{n}' for n in range(len(tts))])):
        MANIFEST[f'tt/{n}'] = save(im, f'tt/{n}.webp')
    for n, city in enumerate(SITE['contact']['cities']):
        im = load(city['image'])
        MANIFEST[f'city/{n}'] = save(cover(im, 800, 400, marker_focus(im)), f'city/{n}.webp')
    for n, ph in enumerate(SITE['about']['photos']):
        im = load(ph)
        if min(im.size) >= 200:
            MANIFEST[f'about/{n}'] = save(cover(alpha_trim(im, tol=10), 1000, 625, focus(im)), f'about/{n}.webp')
    for n, c in enumerate(SITE['services']['cases']):
        # 仿真案例都是白底曲线图，图注要看清：铺满浅色底板 + 允许放大
        MANIFEST[f'svc/{n}'] = save(place(alpha_trim(load(c), tol=10), 900, 560, pad=0.03,
                                          plate=(255, 255, 255), key=f'svc/{n}', src=c), f'svc/{n}.webp')
    v = SITE['home']['video']
    MANIFEST['poster/home'] = save(cover(load(v['poster']), 1280, 720), 'poster/home.webp')
    for slug, p in SITE['products'].items():
        for n, vid in enumerate(p['videos']):
            if vid['poster']:
                im = load(vid['poster'])
                MANIFEST[f'poster/{slug}/{n}'] = save(cover(im, 1280, 720, focus(im)), f'poster/{slug}-{n}.webp')
    json.dump(MANIFEST, open(os.path.join(ROOT, 'cache', 'img_manifest.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(OUT) for f in fs)
    print(f'{len(MANIFEST)} derived images, {total / 1048576:.1f} MB')
    if LOWRES:
        print('原图分辨率不足（需放大才能铺满，建议换图）：')
        for k, s, f in sorted(LOWRES, key=lambda r: -r[2]):
            print(f'  {f:>4}x  {k:24s} {s}')


def marker_focus(im):
    """地图截图：把红色定位针作为裁剪中心。"""
    a = np.asarray(im.convert('RGB'), dtype=np.int16)
    m = (a[..., 0] > 140) & (a[..., 0] - a[..., 1] > 55) & (a[..., 0] - a[..., 2] > 55)
    if m.sum() < 20:
        return (0.5, 0.5)
    ys, xs = np.where(m)
    cx, cy = float(np.median(xs)) / max(1, im.width - 1), float(np.median(ys)) / max(1, im.height - 1)
    return (min(0.82, max(0.18, cx)), min(0.82, max(0.18, cy)))


if __name__ == '__main__':
    main()
