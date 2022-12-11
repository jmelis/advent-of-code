import sys

input = open('input.txt').read().strip()

grid = []
for l in input.split("\n"):
    grid.append([int(i) for i in l])

HSIZE = len(grid)
VSIZE = len(grid[0])

print((HSIZE, VSIZE))

transforms = [
    lambda i, j: (i, j),
    lambda i, j: (i, VSIZE - j - 1),
    lambda i, j: (j, i),
    lambda i, j: (VSIZE - j - 1, i),
]

def get_visible(l):
    visible = []
    max_item = -1
    for x, y, v in l:
        if v > max_item:
            max_item = v
            visible.append((x, y))
    return visible

all_visible = []
for t in transforms:
    for i in range(HSIZE):
        items = []
        for j in range(VSIZE):
            x, y = t(i,j)
            items.append((x, y, grid[x][y]))
        all_visible.append(get_visible(items))

visible_set = set()
for sublist in all_visible:
    visible_set.update(sublist)

print(len(visible_set))

