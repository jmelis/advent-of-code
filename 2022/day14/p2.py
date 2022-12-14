import sys
import os

data = open('input.txt').read().strip().split("\n")


def render(rocks, resting_sand, current_pos=(-1,-1)):
    y_min = 0
    y_max = max([r[1] for r in rocks]) + 10
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
        x1 = scan[i][0]
        x2 = scan[i+1][0]
        y1 = scan[i][1]
        y2 = scan[i+1][1]
        xvals = sorted([x1,x2])
        yvals = sorted([y1, y2])
        for x in range(xvals[0], xvals[1]+1):
            for y in range(yvals[0], yvals[1]+1):
                rocks.add((x,y))

ground = max([r[1] for r in rocks]) + 1
end = False
current_pos = (500,0)
while True:
    if end:
        break

    # os.system("clear")
    # print(current_pos)
    # render(rocks, resting_sand, current_pos)
    # input()
    current_pos = (500,0)
    while True:
        # stop if there's a sand at the origin
        if (500,0) in resting_sand:
            end = True
            break
        # stop if we've reached the ground
        if current_pos[1] == ground:
            resting_sand.add(current_pos)
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

