import numpy as np

x = np.array([1,0,0])
y = np.array([0,1,0])
z = np.array([0,0,1])

dirs = {
    tuple(x): 'x',
    tuple(y): 'y',
    tuple(z): 'z',
    tuple(-x): '-x',
    tuple(-y): '-y',
    tuple(-z): '-z',
}

rotations = []
for i in [x, -x, y, -y, z, -z]:
    for j in [x, -x, y, -y, z, -z]:
        if np.array_equal(i,j) or np.array_equal(i,-j):
            continue
        ti = dirs[tuple(i)]
        tj = dirs[tuple(j)]
        tk = dirs[tuple(np.cross(i, j))]
        rotations.append((ti, tj, tk))

def rotate(p,rotation):
    px, py, pz = p
    val_dict = {
        'x': px, '-x': -px,
        'y': py, '-y': -py,
        'z': pz, '-z': -pz,
    }
    return np.array([val_dict[rotation[i]] for i in range(3)])

input = open('input.txt').read()
scanners_raw = input.split("\n\n")
scanners = []
for scanner_raw in scanners_raw:
    lines = scanner_raw.splitlines()
    points = set()
    for line in lines[1:]:
        point = tuple([int(i) for i in line.split(',')])
        points.add(point)
    scanners.append(points)


def match(s1, s2):
    for r in rotations:
        s2r = [rotate(p, r) for p in s2]
        for p2 in s2r:
            for p1 in s1:
                tv = np.array(p1) - p2
                s2rt = set([tuple(p+tv) for p in s2r])
                if len(s1 & s2rt) >= 12:
                    return (r, tuple(tv), s2rt)
    return False


mapped = set([0])
points = set(scanners[0])
positions = [(0,0,0)]

while True:
    print(len(mapped))
    for index, s in enumerate(scanners):
        if index in mapped:
            continue
        print(['test', index])
        m = match(points, s)
        if m:
            points.update(m[2])
            mapped.add(index)
            positions.append(m[1])
            print(['match', index, len(scanners)-len(mapped)])
    if len(mapped) == len(scanners):
        break

print(positions)
