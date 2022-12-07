from collections import deque, defaultdict

input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")

input = """VJ-nx
start-sv
nx-UL
FN-nx
FN-zl
end-VJ
sv-hi
em-VJ
start-hi
sv-em
end-zl
zl-em
hi-VJ
FN-em
start-VJ
jx-FN
zl-sv
FN-sv
FN-hi
nx-end""".split("\n")

graph = defaultdict(list)
for line in input:
    s, d = line.split('-')
    if d != 'start' and s != 'end':
        graph[s].append(d)
    if s != 'start' and d != 'end':
        graph[d].append(s)

print(graph)

def can_visit(path, n):
    if n.isupper():
        return True

    visited = defaultdict(int)
    for p in path:
        if p.islower():
            visited[p] += 1
    visited[n] += 1

    if max(visited.values()) > 2:
        return False

    if list(visited.values()).count(2) > 1:
        return False
    
    return True

paths = []
def discover(node, path=None):
    global graph, paths

    if path is None:
        path = [node]

    for n in graph[node]:
        if n == 'end':
            paths.append(path + [n])
        else:
            if can_visit(path, n):
                discover(n, path + [n])

discover('start')
for p in paths:
    print(",".join(p))
print(len(paths))


