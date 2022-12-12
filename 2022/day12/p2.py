data = open('input.txt').read().strip().split("\n")

class Nodes:
    def __init__(self):
        self.end_node = None
        self.nodes = []

    def __repr__(self):
        return str([n for n in self.nodes])

    def add(self, node):
        self.nodes.append(node)
        if node.end_node:
            self.end_node = node

    def get(self, row, col):
        for n in self.nodes:
            if n.row == row and n.col == col:
                return n
        return None

    def unvisited_neighbours(self, origin_node):
        r = origin_node.row
        c = origin_node.col
        v = origin_node.val

        candidates = [
            self.get(r-1, c), # up
            self.get(r, c+1), # right
            self.get(r+1, c), # down
            self.get(r, c-1), # left
        ]

        ns = []
        for node in candidates:
            if not node:
                continue

            if node.visited:
                continue

            if node.val > v+1:
                continue

            ns.append(node)

        return ns

    def next_node(self, origin_node):
        ns = [n for n in self.nodes if n.distance is not None and n.visited is False]

        if not ns:
            return None

        ns.sort(key=lambda n: n.distance)
        return ns[0]


    def walk(self, origin_node):
        for n in self.nodes:
            n.distance = None
            n.visited = False

        origin_node.distance = 0
        current_node = origin_node
        while True:
            for neighbour in nodes.unvisited_neighbours(current_node):
                if neighbour.distance is None or neighbour.distance > current_node.distance + 1:
                    neighbour.distance = current_node.distance + 1

            current_node.visited = True

            if current_node == nodes.end_node:
                break

            current_node = nodes.next_node(current_node)
            if current_node is None:
                break

    def start_nodes(self):
        return [n for n in self.nodes if n.val == 97]

class Node:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.end_node = False
        self.visited = False
        self.distance = None

        if val == 'S':
            val = 'a'
        elif val == 'E':
            self.end_node = True
            val = 'z'

        self.val = ord(val)

    def __repr__(self):
        return str((self.row, self.col, self.val, self.distance))



# load data
nodes = Nodes()
for row, line in enumerate(data):
    for col, val in enumerate(line):
        nodes.add(Node(row, col, val))

start_nodes = nodes.start_nodes()
mindist = 1000
for i in range(len(start_nodes)):
    nodes.walk(start_nodes[i])
    print("{}/{}: {}".format(i+1, len(start_nodes), nodes.end_node.distance))
    if nodes.end_node.distance:
        mindist = min(mindist, nodes.end_node.distance)

print(mindist)
print(nodes.end_node)
