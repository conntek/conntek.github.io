"""压缩 docs/public/images 里的大图，文件名和扩展名不变（md 引用不用改）。

规则：大于 200KB 的图，长边缩到 1400px 以内；PNG 量化为 256 色（保留透明），JPG 质量 82。
只有压缩后小于原文件 90% 才替换。可重复运行，已压过的图不会再变大。
"""
import os, sys
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'public', 'images')
MIN_BYTES = 200 * 1024
MAX_SIDE = 1400

before = after = n = 0
for dp, _, fns in os.walk(ROOT):
    for fn in fns:
        path = os.path.join(dp, fn)
        ext = fn.lower().rsplit('.', 1)[-1]
        size = os.path.getsize(path)
        if size < MIN_BYTES or ext not in ('png', 'jpg', 'jpeg'):
            continue
        im = Image.open(path)
        im.load()
        if max(im.size) > MAX_SIDE:
            im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        tmp = path + '.tmp'
        if ext == 'png':
            if im.mode not in ('RGBA', 'RGB'):
                im = im.convert('RGBA' if 'transparency' in im.info or im.mode in ('LA', 'P') else 'RGB')
            q = im.quantize(256, method=Image.Quantize.FASTOCTREE) if im.mode == 'RGBA' else im.quantize(256)
            q.save(tmp, 'PNG', optimize=True)
        else:
            im.convert('RGB').save(tmp, 'JPEG', quality=82, optimize=True, progressive=True)
        new = os.path.getsize(tmp)
        if new < size * 0.9:
            os.replace(tmp, path)
            before += size
            after += new
            n += 1
            print(f'{size / 1024:7.0f}K -> {new / 1024:6.0f}K  {os.path.relpath(path, ROOT)}')
        else:
            os.remove(tmp)
print(f'compressed {n} images: {before / 1048576:.1f}M -> {after / 1048576:.1f}M')
