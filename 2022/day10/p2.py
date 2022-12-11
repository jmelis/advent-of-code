import sys
data = open('input.txt').read().strip().split("\n")
values = [1]
for line in data:
    if 'noop' in line:
        values.append(values[-1])

    if 'addx' in line:
        values.append(values[-1])
        values.append(values[-1] + int(line.split()[-1]))

strength = 0
cycles = [20, 60, 100, 140, 180, 220]
for c in cycles:
    strength += values[c-1] * c


for i, v in enumerate(values):
    pixel = (i+1) % 40

    if pixel in [v, v+1, v+2]:
        sys.stdout.write('#')
    else:
        sys.stdout.write('.')

    if pixel == 0:
        print()


