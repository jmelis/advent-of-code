import math

input = """F10
N3
F7
R90
F11""".split("\n")

with open('input.txt') as f:
    input = f.read().strip().split()

def rotate(pos, degrees):
    x, y = pos
    radians = math.radians(degrees)
    x1 = int(x * math.cos(radians) - y * math.sin(radians))
    y1 = int(x * math.sin(radians) + y * math.cos(radians))
    return x1, y1

directions = {
    'N': (0,1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'F': (1, 0)
}

pos = [0, 0]
list_pos = []
for line in input:
    action = line[0]
    num = int(line[1:])
    
    if action in ['L', 'R']:
        if action == 'R':
            num = 360 - num
        directions['F'] = rotate(directions['F'], num)
    else:
        pos[0] += directions[action][0]*num
        pos[1] += directions[action][1]*num

    list_pos.append(pos.copy())
print(abs(pos[0]) + abs(pos[1]))


