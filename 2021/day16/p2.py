from collections import deque
from numpy import prod

def to_bin(hexnum):
    return format(int(f"0x{hexnum}", 0), 'b').rjust(len(hexnum)*4, '0')

def readn(string, n):
    if len(string) < n:
        return None, None
    return string[:n], string[n:]

def to_dec(binnum):
    return int(f'0b{binnum}',0)

def read_literal(input):
    groups_left = True
    binnum = ""
    while groups_left:
        group, input = readn(input, 5)
        if group[0] == '0':
            groups_left = False
        binnum += group[1:]
    return to_dec(binnum), input

def read_operator(input):
    return 10

DEBUG = False

Q = deque()
TYPES = ['+', '*', 'min', 'max', 'literal', 'gt', 'lt', 'eq']


class Tree:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, t):
        self.children.append(t)

toptree = None
def process(input, parent=None):    
    if not input:
        return

    if DEBUG: print(['new-packet', len(input)])

    version, input = readn(input, 3)
    version = to_dec(version)

    if DEBUG: print(['version', version])

    packet_type, input = readn(input, 3)
    packet_type = TYPES[to_dec(packet_type)]

    if DEBUG: print(['packet-type', packet_type])

    if packet_type != 'literal':
        node = Tree(packet_type)

        if parent:
            parent.add_child(node)
        else:
            global toptree
            toptree = node

        if DEBUG: print(['operator'])
        length_type, input = readn(input, 1)
        length_type = int(length_type)
        if DEBUG: print(['length-type', length_type])
        if length_type == 0:
            length, input = readn(input, 15)
            length = to_dec(length)
            if DEBUG: print(['length'], length)
            input, rest = readn(input, length)
            while input:
                input = process(input, node)
            input = rest
        else:
            num_packets, input = readn(input, 11)
            num_packets = to_dec(num_packets)
            if DEBUG: print(['num-packets', num_packets])
            for _ in range(num_packets):
                input = process(input, node)
    else:
        literal, input = read_literal(input)
        parent.add_child(Tree(literal))
    return input

assert readn("abcdef", 3) == ("abc", "def")
assert to_bin("D2FE28") == "110100101111111000101000"
assert to_bin("38006F45291200") == "00111000000000000110111101000101001010010001001000000000"
assert to_bin("EE00D40C823060") == "11101110000000001101010000001100100000100011000001100000"
assert to_dec("110") == 6
assert read_literal("101111111000101000") == (2021, '000')

# # input = to_bin("D2FE28")
import sys
input = to_bin(sys.argv[1])
process(input)

# r = Tree('+')
# t = Tree('+')
# t.add_child(Tree(1))
# t.add_child(Tree(2))
# r.add_child(t)
# t = Tree('*')
# t.add_child(Tree(2))
# t.add_child(Tree(2))
# r.add_child(t)
# r.add_child(Tree(3))

def print_tree(tree, n=0):
    print((" "*n)+tree.val)
    for c in tree.children:
        if isinstance(c, Tree):
            print_tree(c, n+2)
        else:
            print((" "*(n+1))+str(c))

def traverse(node):
    # first subtrees
    for c in node.children:
        if isinstance(c, Tree):
            traverse(c)
# TYPES = ['+', '*', 'min', 'max', 'literal', 'gt', 'lt', 'eq']
    if node.val == '+':
        node.val = sum([c.val for c in node.children])
    elif node.val == '*':
        val = 1
        for c in node.children:
            val *= c.val
        node.val = val
    elif node.val == 'min':
        node.val = min([c.val for c in node.children])
    elif node.val == 'max':
        node.val = max([c.val for c in node.children])
    elif node.val == 'gt':
        node.val = 1 if node.children[0].val > node.children[1].val else 0
    elif node.val == 'lt':
        node.val = 1 if node.children[0].val < node.children[1].val else 0
    elif node.val == 'eq':
        node.val = 1 if node.children[0].val == node.children[1].val else 0

traverse(toptree)
print(toptree.val)
