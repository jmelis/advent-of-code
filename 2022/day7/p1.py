import re
import os

input = open('input.txt').read()

class Node:

    def __init__(self, path, parent=None):
        self._children = []
        self.path = path
        self._parent = parent
        self._files_size = 0

    def parent(self):
        return node._parent

    def child(self, p):
        # try to find node
        for c in self._children:
            if os.path.basename(c.path) == p:
                return c

        # not found, create one
        c = Node(os.path.join(self.path, p), self)
        self._children.append(c)

        return c

    def addfile(self, s):
        self._files_size += s

    def __repr__(self):
        return f"{self.path}"

    def dirsize(self):
        totalsize = self._files_size
        for c in self._children:
            totalsize += c.dirsize()
        return totalsize

    def traverse(self, summary=None):
        if summary is None:
            summary = []

        for c in self._children:
            c.traverse(summary)

        summary.append((self.path, self.dirsize()))
        return summary



root = Node('/')
node = root
for l in input.strip().split("\n"):
    if m := re.match(r"\$ cd (.*)", l):
        p = m.group(1)
        if p == '/':
            node = root
        elif p == '..':
            node = node.parent()
        else:
            node = node.child(p)

    elif m := re.match(r"^(\d+)", l):
        node.addfile(int(m.group(1)))

# p1
sum_size = 0
for path, size in root.traverse():
    if size <= 100000:
        sum_size += size
print(sum_size)

# p2
total_disk_size       = 70000000
required_unused_space = 30000000
root_size             = root.dirsize()
current_unused        = total_disk_size - root_size
required_delete       = required_unused_space - current_unused

candidates = []
for path, size in root.traverse():
    if size >= required_delete:
        candidates.append(size)
print(min(candidates))
