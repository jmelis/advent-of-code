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
    if pos[0] < 0 or pos[1] < 0 or pos[0] > DIMROWS-1 or pos[1] > DIMCOLS -1:
        return None
    return data[pos[0]][pos[1]]
    
def basin_size(data, pos, seen = None):
    if seen is None:
        seen = set([pos])

    min_val = val(data, pos)
    min_row, min_col = pos

    # up
    current_row = min_row - 1
    current_col = min_col
    current_val = min_val
    active = True
    while active:
        pos = (current_row, current_col)
        if pos in seen:
            break

        current_val = val(data, pos)
        active = current_val and current_val < 9
        if active:
            seen.add(pos)
            seen = seen.union(basin_size(data, pos, seen))
            current_row -= 1

    # down
    current_row = min_row + 1
    current_col = min_col
    current_val = min_val
    active = True
    while active:
        pos = (current_row, current_col)
        if pos in seen:
            break

        current_val = val(data, pos)
        active = current_val and current_val < 9
        if active:
            seen.add(pos)
            seen = seen.union(basin_size(data, pos, seen))
            current_row += 1

    # left
    current_row = min_row
    current_col = min_col - 1
    current_val = min_val
    active = True
    while active:
        pos = (current_row, current_col)
        if pos in seen:
            break

        current_val = val(data, pos)
        active = current_val and current_val < 9
        if active:
            seen.add(pos)
            seen = seen.union(basin_size(data, pos, seen))
            current_col -= 1

    # right
    current_row = min_row
    current_col = min_col + 1
    current_val = min_val
    active = True
    while active:
        pos = (current_row, current_col)
        if pos in seen:
            break

        current_val = val(data, pos)
        active = current_val and current_val < 9
        if active:
            seen.add(pos)
            seen = seen.union(basin_size(data, pos, seen))
            current_col += 1

    return seen


minpoints = []
for i in range(DIMROWS):
    for j in range(DIMCOLS):
        current_val = val(data,(i,j))
        relative_val = [val(data, p) > current_val for p in around(i,j)]
        if all(relative_val):
            minpoints.append((i,j))

# p = (2,2)
# print(basin_size(data, p))

basins = []
for p in minpoints:
    basins.append(len(basin_size(data, p)))

val = 1
for i in sorted(basins, reverse=True)[:3]:
    val *= i
print(val)
