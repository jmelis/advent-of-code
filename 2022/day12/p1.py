data = open('input.txt').read().strip().split("\n")

nodes = []
start_node = None
end_node = None


class Nodes:
    def __init__(self):
        self._start_node = None
        self._end_node = None
        self.nodes = []

    def __repr__(self):
        return str([n for n in self.nodes])

    def add(self, node):
        self.nodes.append(node)

    @property
    def start_node(self):
        if self._start_node:
            return self._start_node

        for n in self.nodes:
            if n.start_node:
                self._start_node = n
                return n

    @property
    def end_node(self):
        if self._end_node:
            return self._end_node

        for n in self.nodes:
            if n.end_node:
                self._end_node = n
                return n

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


class Node:
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.start_node = False
        self.end_node = False
        self.visited = False
        self.distance = None

        if val == 'S':
            self.start_node = True
            self.distance = 0
            val = 'a'
        elif val == 'E':
            self.end_node = True
            val = 'z'

        self.val = ord(val)

    def __repr__(self):
        return str((self.row, self.col, self.val, self.distance))


nodes = Nodes()
for row, line in enumerate(data):
    for col, val in enumerate(line):
        nodes.add(Node(row, col, val))

current_node = nodes.start_node
print(current_node)
while True:
    print(current_node)
    for neighbour in nodes.unvisited_neighbours(current_node):
        if neighbour.distance is None or neighbour.distance > current_node.distance + 1:
            neighbour.distance = current_node.distance + 1

    current_node.visited = True

    if current_node == nodes.end_node:
        print("visited end_node!")
        break

    current_node = nodes.next_node(current_node)
    if current_node is None:
        print("current node is None!")
        break
