from collections import deque, defaultdict

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

def mt(n):
    return 2 if n.isupper() else 1

graph = defaultdict(list)
for line in input:
    s, d = line.split('-')
    if d != 'start' and s != 'end':
        graph[s].append(d)
    if s != 'start' and d != 'end':
        graph[d].append(s)

print(graph)

paths = []
def discover(node, path=None):
    global graph, paths

    if path is None:
        path = [node]

    for n in graph[node]:
        if n == 'end':
            paths.append(path + [n])
        else:
            if n.isupper() or n not in path:
                discover(n, path + [n])

discover('start')
for p in paths:
    print(",".join(p))
print(len(paths))
