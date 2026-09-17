"""把 codex 生成的黑底白线首屏背景图转成透明 WebP。

黑底线稿 → 亮度即不透明度（alpha = 亮度），颜色保留原色并按 alpha 反预乘，
叠到深色页面上不会出现黑框或灰边。红色点缀保留。
用法：python scripts/motif/make_hero_bg.py [源 png] [输出 webp]
"""
import os, sys
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'content', 'motif-src', 'hero-wafer-arm.png')
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'docs', 'public', 'img', 'motif', 'hero-wafer-arm.webp')

im = Image.open(src).convert('RGB')
a = np.asarray(im, dtype=np.float32) / 255.0
lum = a.max(axis=2)                                   # 用最大通道，红色点缀不会被当成暗部抠掉
alpha = np.clip((lum - 0.04) / 0.96, 0, 1)            # 纯黑底（含压缩噪点）完全透明
rgb = np.where(alpha[..., None] > 0, np.clip(a / np.maximum(lum[..., None], 1e-3), 0, 1), 0)
rgba = np.dstack([rgb, alpha])
res = Image.fromarray((rgba * 255).astype(np.uint8), 'RGBA')
if res.width > 2400:
    res = res.resize((2400, round(res.height * 2400 / res.width)), Image.LANCZOS)
os.makedirs(os.path.dirname(out), exist_ok=True)
res.save(out, 'WEBP', quality=86, method=6)
print(out, res.size, os.path.getsize(out) // 1024, 'KB')
