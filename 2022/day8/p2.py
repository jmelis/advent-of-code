import sys
import math

input = open('input.txt').read().strip()


grid = []
for l in input.split("\n"):
    grid.append([int(i) for i in l])

SIZE = len(grid)

transforms = [
    lambda i, j: (i-1, j), # up
    lambda i, j: (i, j-1), # left
    lambda i, j: (i, j+1), # right
    lambda i, j: (i+1, j), # down
]

def scenic_score(grid, start_x, start_y):
    tree_height = grid[start_x][start_y]

    scores = []
    for t in transforms:
        x = start_x
        y = start_y

        score = 0
        while True:
            x, y = t(x, y)

            # stop if we are out of bounds
            if x < 0 or x > SIZE - 1 or y < 0 or y > SIZE - 1:
                break

            score += 1

            # stop if we reach a tree of same height
            if grid[x][y] >= tree_height:
                break

        scores.append(score)

    return math.prod(scores)



max_score = -1
for i in range(SIZE):
    for j in range(SIZE):
        score = scenic_score(grid, i, j)
        if score > max_score:
            max_score = score
print(max_score)
