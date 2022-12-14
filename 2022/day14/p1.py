import sys
import os

data = open('input.txt').read().strip().split("\n")


def render(rocks, resting_sand, current_pos=(-1,-1)):
    y_min = 0
    y_max = max([r[1] for r in rocks]) + 1
    x_min = min([r[0] for r in rocks]) - 1
    x_max = max([r[0] for r in rocks]) + 1

    for y in range(y_min, y_max+1):
        for x in range(x_min, x_max+1):
            if (x,y) in rocks:
                char = "#"
            elif (x,y) in resting_sand or (x,y) == current_pos:
                char = "o"
            else:
                char = "."
            sys.stdout.write(char)
        print()

rocks = set([])
resting_sand = set([])
for l in data:
    scan = []
    for chunk in l.split(" -> "):
        x, y = chunk.split(",")
        scan.append((int(x), int(y)))
    for i in range(len(scan)-1):
        if scan[i][0] == scan[i+1][0]:
            x = scan[i][0]
            y1 = scan[i][1]
            y2 = scan[i+1][1]
            yvals = sorted([y1, y2])
            for y in range(yvals[0], yvals[1]+1):
                rocks.add((x,y))
        else:
            y = scan[i][1]
            x1 = scan[i][0]
            x2 = scan[i+1][0]
            xvals = sorted([x1,x2])
            for x in range(xvals[0], xvals[1]+1):
                rocks.add((x,y))




end = False
while True:
    if end:
        break
    current_pos = (500,0)

    # os.system("clear")
    # render(rocks, resting_sand, current_pos)
    # input()
    while True:

        # stop if we are out of bounds
        if current_pos[1] > max([r[1] for r in rocks]):
            end = True
            break

        # attempt to go down
        down = (current_pos[0], current_pos[1]+1)
        if down not in rocks and down not in resting_sand:
            current_pos = down
        else:
            # attempt to go left or right
            left = (current_pos[0]-1, current_pos[1]+1)
            right = (current_pos[0]+1, current_pos[1]+1)
            if left not in rocks and left not in resting_sand:
                current_pos = left
            elif right not in rocks and right not in resting_sand:
                current_pos = right
            else:
                resting_sand.add(current_pos)
                break
print(len(resting_sand))

