"""首页上半部整屏背景：一整片大晶圆（替代原来的等高线）。

要求（王超 2026-09-17）：一个大的圆，上面的切割线整体旋转一定角度，做成首页上半部整页的背景，一眼看出来就是芯片晶圆。
画法：晶圆外圆 + 底部定位缺口 + 边缘排除区虚线圈；圆内是旋转后的 die 网格（每个 die 一个方框，
相邻方框之间的空隙就是切割道），每 4×4 个 die 一个曝光场用稍亮的切割道中线标出；
被圆周截断的边缘 die 由裁剪自然形成；中心附近点亮一颗 die（品牌红极淡填充）作为视觉锚点。纯线描为主。
用法：python scripts/motif/gen_hero_wafer.py docs/public/img/motif
"""
import math, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else 'docs/public/img/motif'
W, H = 1600, 1000
CX, CY, R = 1060, 470, 610      # 大圆：圆心偏右，文字区只压到圆的左缘
PITCH, STREET = 34.0, 5.0       # die 间距、切割道宽
ANGLE = 30                      # 切割线整体旋转角度（度）
EXCL = R - 16                   # 边缘排除区
NOTCH = 14                      # 定位缺口半宽


def f(v):
    return ('%.1f' % v).rstrip('0').rstrip('.')


# die 网格在旋转坐标系里生成（以圆心为原点），整体 rotate
k = int(R / PITCH) + 2
s = PITCH - STREET
dies, field = [], []
for i in range(-k, k):
    for j in range(-k, k):
        x0 = i * PITCH + STREET / 2
        y0 = j * PITCH + STREET / 2
        # 只生成与圆相交的 die（四角有任一在圆内，或中心在圆内）
        pts = [(x0, y0), (x0 + s, y0), (x0, y0 + s), (x0 + s, y0 + s), (x0 + s / 2, y0 + s / 2)]
        if not any(x * x + y * y <= (R + PITCH) ** 2 for x, y in pts):
            continue
        dies.append('M%s %sh%sv%sh-%sz' % (f(x0), f(y0), f(s), f(s), f(s)))
for i in range(-k, k + 1):
    if i % 4:
        continue
    v = i * PITCH
    h = math.sqrt(max(0.0, R * R - v * v))
    if h:
        field.append('M%s %sV%s' % (f(v), f(-h), f(h)))
        field.append('M%s %sH%s' % (f(-h), f(v), f(h)))

# 点亮的一颗 die（靠近中心、偏上）
hx, hy = 2 * PITCH + STREET / 2, -3 * PITCH + STREET / 2
lit = 'M%s %sh%sv%sh-%sz' % (f(hx), f(hy), f(s), f(s), f(s))

# 外圆带底部缺口（缺口朝下，不随网格旋转）
a = math.asin(NOTCH / R)
p1 = (CX + R * math.sin(a), CY + R * math.cos(a))
p2 = (CX - R * math.sin(a), CY + R * math.cos(a))
outline = ('M%s %sA%d %d 0 1 1 %s %s' % (f(p1[0]), f(p1[1]), R, R, f(p2[0]), f(p2[1]))
           + 'A%d %d 0 0 0 %s %s' % (NOTCH, NOTCH, f(p1[0]), f(p1[1])))

rot = 'translate(%s %s) rotate(%d)' % (f(CX), f(CY), ANGLE)
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" fill="none" stroke="#fff" stroke-width="1" preserveAspectRatio="xMidYMid slice">' % (W, H)
       + '<defs><clipPath id="w"><path d="%s"/></clipPath>' % outline
       + '<radialGradient id="g" cx="%s" cy="%s" r="%s" gradientUnits="userSpaceOnUse">' % (f(CX), f(CY), f(R))
       + '<stop offset="0" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>'
       + '<path d="%s" fill="url(#g)" stroke="none"/>' % outline
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".95" stroke-width="1.5" d="%s"/>' % outline
       + '<g clip-path="url(#w)">'
       + '<g transform="%s">' % rot
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".5" d="%s"/>' % ''.join(dies)
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".75" stroke-dasharray="2 4" d="%s"/>' % ''.join(field)
       + '<path d="%s" fill="#C30D23" fill-opacity=".55" stroke="#ff5a6a" stroke-opacity=".9" vector-effect="non-scaling-stroke"/>' % lit
       + '</g>'
       + '<circle vector-effect="non-scaling-stroke" cx="%s" cy="%s" r="%s" stroke-opacity=".6" stroke-dasharray="3 7"/>' % (f(CX), f(CY), f(EXCL))
       + '</g></svg>')
open(OUT + '/hero-wafer.svg', 'w', encoding='utf-8', newline='\n').write(svg)
print('hero-wafer.svg', len(svg) // 1024, 'KB', len(dies), 'dies')
