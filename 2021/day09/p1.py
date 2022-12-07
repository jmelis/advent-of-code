


input = """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

DIMROWS = len(input)
DIMCOLS = len(input[0])

data = [[int(i) for i in r] for r in input]

def around(row, col):
    points = []
    
    # up
    if row > 0:
        points.append((row-1, col))

    # down
    if row < DIMROWS-1:
        points.append((row+1, col))

    # left
    if col > 0:
        points.append((row, col-1))

    # right
    if col < DIMCOLS-1:
        points.append((row, col+1))

    return points


def val(data, pos):
    return data[pos[0]][pos[1]]
    

total = 0
for i in range(DIMROWS):
    for j in range(DIMCOLS):
        current_val = val(data,(i,j))
        relative_val = [val(data, p) > current_val for p in around(i,j)]
        if all(relative_val):
            total += current_val + 1

print(total)
