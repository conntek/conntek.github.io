"""Generate footer-scroll.svg (animated) and footer-scroll-still.svg (static).
viewBox 3200 x 120, composition centred; strokes are non-scaling (1px on screen)."""
import math, random, sys

OUT = sys.argv[1]
W, H = 3200, 120
rnd = random.Random(7)


def f(v):
    return ('%.1f' % v).rstrip('0').rstrip('.')


def jag(pts, amp=1.2, step=14):
    """Subdivide a polyline and add small jitter -> hand-drawn feel."""
    out = []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
        for i in range(n):
            t = i / n
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            if i:
                x += rnd.uniform(-amp, amp) * 0.4
                y += rnd.uniform(-amp, amp)
            out.append((x, y))
    out.append(pts[-1])
    return out


def d(pts):
    return 'M' + ' L'.join(f(x) + ' ' + f(y) for x, y in pts)


def ridge(x0, x1, base, amp, seed, step=40):
    r = random.Random(seed)
    pts = []
    ph = r.uniform(0, 6)
    x = x0
    while x <= x1 + 1e-6:
        y = base - amp * (0.55 * math.sin(x / 210 + ph) + 0.3 * math.sin(x / 83 + ph * 2) + 0.15 * r.uniform(-1, 1))
        pts.append((x, min(119.5, y)))
        x += step
    return pts


paths = []  # (opacity, d)

# ---- far continuous ridges (whole width, keeps the old footer feeling) ----
far = ridge(0, 900, 104, 7, 1) + [(960, 98), (1010, 86)]
paths.append((0.16, d(jag(far, 1.0))))
far_r = [(2280, 100), (2340, 103)] + ridge(2380, W, 104, 7, 2)
paths.append((0.16, d(jag(far_r, 1.0))))
low = ridge(0, 1000, 114, 4, 3) + [(1040, 112)]
paths.append((0.10, d(jag(low, 0.6))))
low_r = [(2320, 113)] + ridge(2360, W, 114, 4, 4)
paths.append((0.10, d(jag(low_r, 0.6))))

# ---- steep layered peaks (back layer) ----
back = [(1010, 86), (1052, 70), (1072, 74), (1112, 34), (1124, 40), (1158, 10), (1170, 18),
        (1182, 6), (1204, 38), (1216, 32), (1246, 60), (1268, 46), (1290, 56), (1318, 30),
        (1336, 36), (1352, 22), (1392, 16), (1418, 4), (1432, 14), (1446, 10), (1478, 44),
        (1494, 38), (1528, 64), (1560, 58), (1610, 78), (1660, 84), (1720, 94)]
paths.append((0.20, d(jag(back, 1.3, 10))))

# ---- middle layer: the cliff pair that frames the fall ----
mid_l = [(1040, 114), (1086, 100), (1120, 84), (1150, 58), (1166, 64), (1196, 34), (1212, 42),
         (1244, 26), (1262, 36), (1290, 30), (1316, 20), (1340, 24), (1358, 28), (1364, 34),
         (1368, 48), (1362, 60), (1346, 76), (1334, 96), (1322, 120)]
paths.append((0.34, d(jag(mid_l, 1.1, 9))))
mid_r = [(1440, 120), (1416, 96), (1400, 76), (1388, 58), (1384, 42), (1382, 30), (1396, 22), (1408, 26),
         (1426, 14), (1444, 30), (1462, 50), (1482, 46), (1520, 72), (1570, 86), (1640, 96), (1700, 104)]
paths.append((0.34, d(jag(mid_r, 1.1, 9))))

# ---- texture strokes on rock faces (short dry-brush lines) ----
tex = []
for (x, y, dx, dy) in [(1200, 40, -8, 26), (1248, 32, -6, 22), (1318, 26, -5, 30), (1340, 30, -8, 32),
                       (1402, 30, 6, 30), (1428, 20, 7, 24), (1450, 36, 9, 22), (1156, 64, -10, 22)]:
    tex.append(d(jag([(x, y), (x + dx, y + dy)], 0.8, 6)))
paths.append((0.13, ' '.join(tex)))

# ---- cloud wisps crossing the peaks ----
wisp = []
for (x0, x1, y) in [(1100, 1190, 70), (1120, 1160, 74), (1456, 1566, 60), (1500, 1544, 64)]:
    pts = [(x0 + (x1 - x0) * t / 10, y + 1.2 * math.sin(t / 10 * math.pi)) for t in range(11)]
    wisp.append(d(pts))
paths.append((0.12, ' '.join(wisp)))

# ---- foothill with a chip-shaped terrace ----
foot = [(1700, 104), (1730, 98), (1760, 92), (1778, 90)]
paths.append((0.30, d(jag(foot, 0.6, 8))))
foot2 = [(1922, 90), (1946, 96), (1990, 104), (2040, 108), (2090, 106)]
paths.append((0.30, d(jag(foot2, 0.6, 8))))
# chip: a square package seen obliquely, sitting on the plateau like a terrace
A, B, C, D = (1812, 94), (1872, 94), (1896, 80), (1836, 80)  # front-left, front-right, back-right, back-left
paths.append((0.36, d([A, B, C, D, A])))
# thin side face (package thickness)
paths.append((0.22, d([(1812, 94), (1812, 97), (1872, 97), (1872, 94)]) + ' ' + d([(1872, 97), (1896, 83), (1896, 80)])))
def lerp(p, q, t):
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
# die inset
dA, dB, dC, dD = [lerp(lerp(A, C, .5), P, .42) for P in (A, B, C, D)]
paths.append((0.22, d([dA, dB, dC, dD, dA])))
# pins on the two slanted sides (left A-D, right B-C), pointing outward like terrace steps
pins = []
for i in range(5):
    t = (i + 0.5) / 5
    x, y = lerp(A, D, t); pins.append('M%s %s L%s %s' % (f(x), f(y), f(x - 6), f(y + 0.5)))
    x, y = lerp(B, C, t); pins.append('M%s %s L%s %s' % (f(x), f(y), f(x + 6), f(y - 0.5)))
paths.append((0.28, ' '.join(pins)))
# plateau lips and stepped terraces below
paths.append((0.30, d([(1778, 90), (1800, 94)]) + ' ' + d([(1908, 88), (1922, 90)])))
terr = []
for k, (a, b, y) in enumerate([(1770, 1930, 102), (1752, 1956, 107), (1732, 1986, 112)]):
    pts = [(a + (b - a) * t / 12, y + 0.8 * math.sin(t / 12 * math.pi * 2 + k)) for t in range(13)]
    terr.append(d(pts))
paths.append((0.14, ' '.join(terr)))

# ---- distant ridge with a small robot arm on its crest ----
dist = [(2060, 110), (2110, 96), (2150, 84), (2190, 76), (2214, 74), (2240, 78), (2280, 92), (2340, 103)]
paths.append((0.22, d(jag(dist, 0.8, 10))))
rb = 2212  # base x on crest (y ~ 74)
arm = [
    'M%s 74 L%s 70 L%s 70 L%s 74' % (f(rb - 7), f(rb - 4), f(rb + 4), f(rb + 7)),  # base
    'M%s 70 L%s 46' % (f(rb), f(rb - 6)),        # lower arm
    'M%s 46 L%s 36' % (f(rb - 6), f(rb + 16)),   # upper arm
    'M%s 36 L%s 44' % (f(rb + 16), f(rb + 21)),  # wrist
    'M%s 44 L%s 49 M%s 44 L%s 48' % (f(rb + 21), f(rb + 18), f(rb + 21), f(rb + 26)),  # gripper
]
paths.append((0.30, ' '.join(arm)))
joints = '<circle cx="%s" cy="46" r="2"/><circle cx="%s" cy="36" r="1.6"/>' % (f(rb - 6), f(rb + 16))

# ---- waterfall ----
fall_x = [1371, 1376, 1380]
strands = []
for i, x in enumerate(fall_x):
    # lip curve out of the notch, then a nearly straight drop
    strands.append('M%s 30 Q%s 33 %s 40 L%s 108' % (f(x - 3), f(x), f(x + 0.3), f(x + 1.2 * (i - 1))))
mist = 'M1352 111 Q1376 104 1400 111 M1360 115 Q1376 111 1392 115 M1340 117 Q1350 115 1358 117 M1396 117 Q1404 115 1412 117'


def svg(animated):
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMax meet" '
         'fill="none" stroke="#fff" stroke-width="1" stroke-linejoin="round" stroke-linecap="round">' % (W, H)]
    s.append('<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="30" x2="0" y2="112">'
             '<stop offset="0" stop-color="#fff" stop-opacity=".55"/>'
             '<stop offset=".6" stop-color="#fff" stop-opacity=".4"/>'
             '<stop offset=".88" stop-color="#C30D23" stop-opacity=".45"/>'
             '<stop offset="1" stop-color="#C30D23" stop-opacity="0"/></linearGradient></defs>')
    if animated:
        s.append('<style>.f{stroke-dasharray:18 5 5 8;animation:m 2.6s linear infinite}'
                 '.f2{stroke-dasharray:11 9 22 6;animation-name:m2;animation-duration:3.4s}.f3{stroke-opacity:.6;animation-duration:2.2s}'
                 '@keyframes m{to{stroke-dashoffset:-36}}@keyframes m2{to{stroke-dashoffset:-48}}'
                 '@media (prefers-reduced-motion:reduce){.f{animation:none}}</style>')
    s.append('<g vector-effect="non-scaling-stroke">')
    for op, dd in paths:
        s.append('<path vector-effect="non-scaling-stroke" stroke-opacity="%s" d="%s"/>' % (f(op), dd))
    s.append('<g stroke-opacity=".3" vector-effect="non-scaling-stroke">%s</g>' % joints.replace('<circle', '<circle vector-effect="non-scaling-stroke"'))
    s.append('</g>')
    # static faint guide of the fall (always visible, so a paused frame still reads as water)
    s.append('<path vector-effect="non-scaling-stroke" stroke="url(#g)" stroke-opacity=".35" d="%s"/>' % strands[1])
    for i, st in enumerate(strands):
        cls = 'f' + ('' if i == 0 else ' f%d' % (i + 1))
        attrs = ' class="%s"' % cls if animated else ' stroke-dasharray="18 5 5 8"'
        s.append('<path vector-effect="non-scaling-stroke" stroke="url(#g)"%s d="%s"/>' % (attrs, st))
    s.append('<path vector-effect="non-scaling-stroke" stroke-opacity=".16" d="%s"/>' % mist)
    s.append('</svg>')
    return ''.join(s)


open(OUT + '/footer-scroll.svg', 'w', encoding='utf-8', newline='\n').write(svg(True))
open(OUT + '/footer-scroll-still.svg', 'w', encoding='utf-8', newline='\n').write(svg(False))
print('ok')
