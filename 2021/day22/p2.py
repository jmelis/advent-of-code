import re

class Cube:
    def __init__(self, on, x1, x2, y1, y2, z1, z2):
        self.on = on
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.z1 = int(z1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.z2 = int(z2)

    def volume(self):
        return (self.x2 - self.x1 + 1)*(self.y2 - self.y1 + 1)*(self.z2 - self.z1 + 1)

    def __repr__(self):
        return f"{self.on} [({self.x1},{self.y1},{self.z1}),({self.x2},{self.y2},{self.z2})]"

    def intersection(self, other):
        intersects = (other.x2 >= self.x1 and other.x1 <= self.x2 and
                      other.y2 >= self.y1 and other.y1 <= self.y2 and
                      other.z2 >= self.z1 and other.z1 <= self.z2)
        
        if not intersects:
            return None

        x1 = max(other.x1, self.x1)
        x2 = min(other.x2, self.x2)

        y1 = max(other.y1, self.y1)
        y2 = min(other.y2, self.y2)

        z1 = max(other.z1, self.z1)
        z2 = min(other.z2, self.z2)

        return Cube(not self.on, x1, x2, y1, y2, z1, z2)

line_re = r'^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$'
cubes = []
for line in open('input.txt').read().splitlines():
    params = list(re.match(line_re, line).groups())
    params[0] = params[0] == 'on'
    cubes.append(Cube(*params))

final_cubes = []
for cube in cubes:
    for fc in final_cubes.copy():
        intersection = fc.intersection(cube)
        if intersection:
            final_cubes.append(intersection)
    if cube.on:
        final_cubes.append(cube)
    
total = 0
for c in final_cubes:
    volume = c.volume()
    if c.on:
        total += volume
    else:
        total -= volume
print(total)
