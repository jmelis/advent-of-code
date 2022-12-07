from collections import deque, defaultdict

# input = open('input.txt').read().splitlines()
input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".splitlines()
around = [(1, 0), (0, 1), (-1, 0), (0, -1)]

DR = len(input)
DC = len(input[0])

nodes = set()
neighbors = defaultdict(list)
cost = {} 

for r, row in enumerate(input):
    for c, val in enumerate(row):
        nodes.add((r, c))
        cost[(r,c)] = int(val)
        for (dr, dc) in around:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < DR and 0 <= cc < DC:
                neighbors[(r,c)].append((rr, cc))

distance = defaultdict(lambda: float('inf'))
distance[(0,0)] = 0
prev_node = {}

notvisited = set(nodes)
# while notvisited:
while notvisited:
    # get the min one
    notvisited_distances = {k: v for k, v in distance.items() if k in notvisited}
    node = min(notvisited_distances, key=notvisited_distances.get)
    notvisited.remove(node)
    for n in neighbors[node]:
        if distance[node] + cost[n] < distance[n]:
            distance[n] = distance[node] + cost[n]

print(distance[(DR-1, DC-1)])
