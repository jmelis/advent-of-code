rotations = [
    # lambda p: (p[0], p[1]),
    # lambda p: (-p[1], p[0]),
    # lambda p: (-p[1], p[0]),
    # lambda p: (-p[0], -p[1]),
    lambda p: (p[1], -p[0]),
]

def t(p, tv):
    x, y = p
    tx, ty = tv
    return (x+tx, y+ty)

def subtract(p1, p2):
    return (p1[0]-p2[0],p1[1]-p2[1])

p1s = set([(1,1), (2,4), (3,3)])
p2s = set([(1,3), (-2,4), (-1, 5)])
# t = (-2, 2)


def match(p1s, p2s):
    for r in rotations:
        p2s_r = [r(p) for p in p2s]
        for p2 in p2s_r:
            for p1 in p1s:
                tv = subtract(p1, p2)
                p2s_rt = set([t(p, tv) for p in p2s_r])
                if p2s_rt == p1s:
                    return (r, tv)
    return False

m = match(p1s, p2s)
if m:
    print(m[1])
