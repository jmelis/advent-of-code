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
    x1 = round(x * math.cos(radians) - y * math.sin(radians))
    y1 = round(x * math.sin(radians) + y * math.cos(radians))
    return x1, y1

directions = {
    'N': (0,1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0),
    'F': (1, 0)
}

pos = [0, 0]
waypoint = [10, 1]

list_pos = []
for line in input:
    action = line[0]
    num = int(line[1:])
    
    if action == 'F':
        pos[0] += waypoint[0]*num
        pos[1] += waypoint[1]*num
    elif action in ['L', 'R']:
        if action == 'R':
            num = 360 - num
        waypoint = rotate(waypoint, num)
    else:
        waypoint = (
            waypoint[0] + directions[action][0]*num,
            waypoint[1] + directions[action][1]*num,
        )

    print([pos, waypoint])
    # list_pos.append(pos.copy())
# print(list_pos)
print(abs(pos[0]) + abs(pos[1]))


