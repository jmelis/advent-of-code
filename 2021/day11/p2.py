from collections import deque

input = """4585612331
5863566433
6714418611
1746467322
6161775644
6581631662
1247161817
8312615113
6751466142
1161847732""".split()

grid = [[int(i) for i in line] for line in input]
for row in grid:
    print("".join([str(i) for i in row]))
print()

AROUND = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
R = len(grid)
C = len(grid[0])

flashes = 0
step = 1
while True:
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

    if len(flashed) == R*C:
        print(step)
        break

    step += 1


