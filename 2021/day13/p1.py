with open('input.txt') as f:
    input = f.read().strip()

points, folds = input.split("\n\n")

points = [tuple(int(i) for i in p.split(',')) for p in points.split()]
folds = [tuple([p[0], int(p[1])]) for p in [tuple(e.split()[2].split('=')) for e in folds.split("\n")]]

X_MAX = max(p[0] for p in points)
Y_MAX = max(p[1] for p in points)

print(X_MAX, Y_MAX)

grid = [[[0,1][bool((x,y) in points)] for x in range(X_MAX+1)] for y in range(Y_MAX+1)] 

def print_grid(grid):
    for y in grid:
        print("".join([' '[bool(i)] for i in y]))

def fold_grid(grid, axis, pos):
    if axis == 'y':
        for y in range(pos+1, len(grid)):
            for x in range(len(grid[0])):
                fold_y = 2*pos - y
                grid[fold_y][x] |= grid[y][x]
        grid = grid[:pos]
    elif axis == 'x':
        for y in range(len(grid)):
            for x in range(pos+1, len(grid[0])):
                fold_x = 2*pos - x
                # import pdb; pdb.set_trace()
                grid[y][fold_x] |= grid[y][x]           
        grid = [row[:pos] for row in grid] 
    return grid


for (axis, pos) in folds:
    grid = fold_grid(grid, axis, pos)
    # break
# print_grid(grid)

print(sum([i for row in grid for i in row]))
# grid = fold_grid(grid, 'x', 5)
print_grid(grid)

# """
# (0,0)   (1,0)   (2,0)   (3,0)   (4,0)   (5,0)   (6,0)   (7,0)   (8,0)   (9,0)
# (0,1)   (1,1)   (2,1)   (3,1)   (4,1)   (5,1)   (6,1)   (7,1)   (8,1)   (9,1)
# (0,2)   (1,2)   (2,2)   (3,2)   (4,2)   (5,2)   (6,2)   (7,2)   (8,2)   (9,2)
# (0,3)   (1,3)   (2,3)   (3,3)   (4,3)   (5,3)   (6,3)   (7,3)   (8,3)   (9,3)
# (0,4)   (1,4)   (2,4)   (3,4)   (4,4)   (5,4)   (6,4)   (7,4)   (8,4)   (9,4)
# (0,5)   (1,5)   (2,5)   (3,5)   (4,5)   (5,5)   (6,5)   (7,5)   (8,5)   (9,5)
# (0,6)   (1,6)   (2,6)   (3,6)   (4,6)   (5,6)   (6,6)   (7,6)   (8,6)   (9,6)
# (0,7)   (1,7)   (2,7)   (3,7)   (4,7)   (5,7)   (6,7)   (7,7)   (8,7)   (9,7)
# (0,8)   (1,8)   (2,8)   (3,8)   (4,8)   (5,8)   (6,8)   (7,8)   (8,8)   (9,8)
# (0,9)   (1,9)   (2,9)   (3,9)   (4,9)   (5,9)   (6,9)   (7,9)   (8,9)   (9,9)
# """

