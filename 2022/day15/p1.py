import re
data = open('input.txt').read().strip().split("\n")
closest_beacons = []

sensors = set([])
beacons = set([])
for l in data:
    m = re.match(r'Sensor at x=(?P<sx>.*), y=(?P<sy>.*): closest beacon is at x=(?P<bx>.*), y=(?P<by>.*)', l)
    sx = int(m.group('sx'))
    sy = int(m.group('sy'))
    bx = int(m.group('bx'))
    by = int(m.group('by'))
    sensors.add((sx, sy))
    beacons.add((bx, by))
    closest_beacons.append((sx, sy, bx, by))

y = 2000000

ranges = []
for cb in closest_beacons:
    sx, sy, bx, by = cb
    xspan = abs(sx - bx)
    yspan = abs(sy - by)
    tspan = xspan + yspan

    xstart = sx-tspan+abs(y-sy)
    xend = sx+tspan-abs(y-sy)
    if xstart <= xend:
        ranges.append((xstart, xend))

ranges = sorted(ranges, key=lambda x: x[0])

new_ranges = []
cr = None
for i in range(len(ranges)-1):
    r1 = ranges[i]
    r2 = ranges[i+1]

    if cr is None:
        cr = r1

    # do they overlap?
    if cr[1] >= r2[0]:
        # yes => extend it (cr = join(r1, r2))
        if r2[1] > cr[1]:
            cr = (cr[0], r2[1])
    else:
        # no => add r1, and cr = r2
        new_ranges.append(cr)
        cr = r2

    # last? => add it
    if i == len(ranges)-2:
        new_ranges.append(cr)

the_sum = 0
for r in new_ranges:
    the_sum += r[1] - r[0] + 1

beacons_in_y = len([b for b in beacons if b[1] == y])
print(the_sum-beacons_in_y)
