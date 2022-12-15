import re
data = open('input.txt').read().strip().split("\n")
closest_beacons = []
sensors = set([])
for l in data:
    m = re.match(r'Sensor at x=(?P<sx>.*), y=(?P<sy>.*): closest beacon is at x=(?P<bx>.*), y=(?P<by>.*)', l)
    sx = int(m.group('sx'))
    sy = int(m.group('sy'))
    bx = int(m.group('bx'))
    by = int(m.group('by'))
    sensors.add((sx, sy))
    closest_beacons.append((sx, sy, bx, by))

empty_spaces = set()
for cb in closest_beacons:
    print(cb)
    sx, sy, bx, by = cb
    xspan = abs(sx - bx)
    yspan = abs(sy - by)
    tspan = xspan + yspan
    for y in range(sy-tspan, sy+tspan+1):
        # y = 7 => x: -1, 17
        for x in range(sx-tspan, sx+tspan+1):
            if abs(sx - x) + abs(sy - y) > tspan:
                continue
            if (x, y) in sensors:
                continue
            if (x, y) == (bx, by):
                continue

            empty_spaces.add((x,y))

print(len([s for s in empty_spaces if s[1] == 10]))
# print(xspan)
