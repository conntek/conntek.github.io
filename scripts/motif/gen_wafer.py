import math, sys
OUT = sys.argv[1]
N = 440; c = N / 2; R = 200; flat_y = c + math.sqrt(R*R - 70*70)  # flat chord half-width 70
p = 17.0; g = 2.2   # die pitch, street width
def f(v): return ('%.1f' % v).rstrip('0').rstrip('.')
def inside(x, y, r=R):
    return (x-c)**2 + (y-c)**2 <= r*r and y <= flat_y
full, part = [], []
off = (p - g) / 2 * 0  # grid origin aligned so wafer centre sits on a street crossing
k = int(R / p) + 2
for i in range(-k, k):
    for j in range(-k, k):
        x0 = c + i*p + g/2; y0 = c + j*p + g/2; s = p - g
        corners = [(x0, y0), (x0+s, y0), (x0, y0+s), (x0+s, y0+s)]
        n_in = sum(inside(x, y) for x, y in corners)
        cmd = 'M%s %sh%sv%sh-%sz' % (f(x0), f(y0), f(s), f(s), f(s))
        if n_in == 4:
            # edge-exclusion: dies outside r=186 drawn fainter
            (full if all(inside(x, y, 184) for x, y in corners) else part).append(cmd)
        elif n_in > 0:
            part.append(cmd)
# reticle fields: every 4 dies a slightly stronger street line
ret = []
for i in range(-3, 4):
    x = c + i*4*p
    h = math.sqrt(max(0, R*R - (x-c)**2))
    ret.append('M%s %sV%s' % (f(x), f(c-h), f(min(c+h, flat_y))))
    y = c + i*4*p
    if y < flat_y:
        w = math.sqrt(max(0, R*R - (y-c)**2))
        ret.append('M%s %sH%s' % (f(c-w), f(y), f(c+w)))
a = math.asin(70 / R)
x1, x2 = c - 70, c + 70
outline = 'M%s %sA%d %d 0 1 0 %s %sZ' % (f(x2), f(flat_y), R, R, f(x1), f(flat_y))
excl = '<circle cx="%s" cy="%s" r="192" stroke-opacity=".18" stroke-dasharray="2 5"/>' % (f(c), f(c))
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" fill="none" stroke="#fff" stroke-width="1">' % (N, N)
       + '<defs><clipPath id="w"><path d="%s"/></clipPath></defs>' % outline
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".7" d="%s"/>' % outline
       + '<g clip-path="url(#w)">' + excl
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".42" d="%s"/>' % ''.join(full)
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".22" d="%s"/>' % ''.join(part)
       + '<path vector-effect="non-scaling-stroke" stroke-opacity=".3" stroke-dasharray="1 3" d="%s"/>' % ''.join(ret)
       + '</g></svg>')
open(OUT + '/wafer.svg', 'w', encoding='utf-8', newline='\n').write(svg)
print(len(svg))
