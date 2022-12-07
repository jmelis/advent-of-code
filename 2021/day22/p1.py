import re

RE = r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$'

lines = open('ex.txt').read().splitlines()



space = set()
for line in lines:
    op, rest = line.split()
    m = re.match(RE, rest)
    x1, x2, y1, y2, z1, z2 = [int(i) for i in m.groups()]
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                if op == 'on':
                    space.add((x,y,z))
                else:
                    try:
                        space.remove((x,y,z))
                    except KeyError:
                        pass

# ans = 611176

print(len(space))
