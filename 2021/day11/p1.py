from collections import deque

input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split()

grid = [[int(i) for i in line] for line in input]
for row in grid:
    print("".join([str(i) for i in row]))
print()

AROUND = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
R = len(grid)
C = len(grid[0])

flashes = 0
for step in range(100):
    Q = deque()
    for r in range(R):
        for c in range(C):
            grid[r][c] += 1
            if grid[r][c] > 9:
                Q.append((r,c))

    flashed = set()
    while Q:
        r, c = Q.popleft()
        if (r, c) in flashed:
            continue
        flashed.add((r, c))
        flashes += 1

        for dr, dc in AROUND:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C:
                grid[rr][cc] += 1
                if grid[rr][cc] > 9:
                    Q.append((rr,cc))

    for r in range(R):
        for c in range(C):
            if grid[r][c] > 9:
                grid[r][c] = 0

    print(f"After step {step+1}:")
    for row in grid:
        print("".join([str(i) for i in row]))
    print()

print(flashes)
