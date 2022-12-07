from copy import deepcopy

input = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

S = [[c for c in line] for line in input]
R = len(S)
C = len(S[0])

AROUND = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
def val(seatmap, r, c):
    if 0 <= r < R and 0 <= c < C:
        return seatmap[r][c]
    return None

seatmap = deepcopy(S)

while True:
    new_seatmap = deepcopy(seatmap)
    for r, row in enumerate(seatmap):
        for c, seat in enumerate(row):
            if seat == '.':
                continue

            around_vals = []
            for (dr, dc) in AROUND:
                i = 1
                while True:
                    v = val(seatmap, r+dr*i, c+dc*i)
                    if not v:
                        break
                    if v in ['#', 'L']:
                        around_vals.append(v) 
                        break
                    i+=1

            if seat == 'L' and '#' not in around_vals:
                new_seatmap[r][c] = '#'
            elif seat == '#' and around_vals.count('#') >= 5:
                new_seatmap[r][c] = 'L'

    print(seatmap == new_seatmap)
    if [i for row in seatmap for i in row] == [i for row in new_seatmap for i in row]:
        break

    seatmap = new_seatmap

print([i for row in seatmap for i in row].count('#'))
