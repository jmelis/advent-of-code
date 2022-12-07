from collections import deque, defaultdict

input = open('input.txt').read().splitlines()
# input = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""".splitlines()

around = [(1, 0), (0, 1), (-1, 0), (0, -1)]

DR = len(input)
DC = len(input[0])

nodes = set()
neighbors = defaultdict(list)
cost = {} 
first_row = ""
for r, row in enumerate(input):
    for c, val in enumerate(row):
        for kr in range(5):
            for kc in range(5):
                nr = r+kr*DR
                nc = c+kc*DC
                nval = 1+(kr+kc+int(val)-1)%9
                nodes.add((nr, nc))
                cost[(nr,nc)] = nval
                for (dr, dc) in around:
                    rr = nr + dr
                    cc = nc + dc
                    if 0 <= rr < DR*5 and 0 <= cc < DC*5:
                        neighbors[(nr,nc)].append((rr, cc))

# for r in range(5*DR):
#     print("".join([str(cost[(r,c)]) for c in range(5*DC)]))

# assert False
distance = defaultdict(lambda: float('inf'))
distance[(0,0)] = 0
prev_node = {}
notvisited = set(nodes)
notvisited_distances = {(0,0): 0}

while notvisited:
    node = min(notvisited_distances, key=notvisited_distances.get)
    notvisited.remove(node)
    del notvisited_distances[node]
    for n in neighbors[node]:
        if distance[node] + cost[n] < distance[n]:
            distance[n] = distance[node] + cost[n]
            notvisited_distances[n] = distance[n]

print(distance[(5*DR-1, 5*DC-1)])
