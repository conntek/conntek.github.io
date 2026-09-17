"""核心价值观 6 张简笔漫画：黑底线稿 → 透明 WebP（亮度即不透明度，红色点缀保留）。

源：content/motif-src/values/values-<key>.png（codex 生成，1200×900，纯黑底白线）
出：docs/public/img/values/<key>.webp（最长边 900）
用法：python scripts/motif/make_values.py
"""
import glob, os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(ROOT, 'content', 'motif-src', 'values')
OUT = os.path.join(ROOT, 'docs', 'public', 'img', 'values')
os.makedirs(OUT, exist_ok=True)

for fn in sorted(glob.glob(os.path.join(SRC, 'values-*.png'))):
    key = os.path.basename(fn)[len('values-'):-4]
    im = Image.open(fn).convert('RGBA')
    # 生成器偶尔自带透明底：先铺黑，统一按黑底线稿处理
    black = Image.new('RGBA', im.size, (0, 0, 0, 255))
    black.alpha_composite(im)
    a = np.asarray(black.convert('RGB'), dtype=np.float32) / 255.0
    lum = a.max(axis=2)
    alpha = np.clip((lum - 0.05) / 0.95, 0, 1)
    rgb = np.where(alpha[..., None] > 0, np.clip(a / np.maximum(lum[..., None], 1e-3), 0, 1), 0)
    res = Image.fromarray((np.dstack([rgb, alpha]) * 255).astype(np.uint8), 'RGBA')
    res.thumbnail((900, 900), Image.LANCZOS)
    out = os.path.join(OUT, key + '.webp')
    res.save(out, 'WEBP', quality=88, method=6)
    print(key, res.size, os.path.getsize(out) // 1024, 'KB')
