class Monkey:
    def __init__(self, items, op, div_by, true_monkey, false_monkey):
        self.items = items
        self.div_by = div_by
        self.op = op
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0
        self.targets = {}

    def get_target(self, w):
        if w in self.targets:
            return self.targets[w]

        nw = self.op(w)
        nw = nw // 3
        if nw % self.div_by == 0:
            target = self.true_monkey
        else:
            target = self.false_monkey

        self.targets[w] = (target, nw)
        return self.targets[w]

    def inspect(self, monkeys):
        items = self.items[:]
        self.inspections += len(items)
        self.items = []

        for w in items:
            target, nw = self.get_target(w)
            monkeys[target].items.append(nw)

monkeys = [
    Monkey([92, 73, 86, 83, 65, 51, 55, 93], lambda x: x*5, 11, 3, 4),
    Monkey([99, 67, 62, 61, 59, 98], lambda x: x*x, 2, 6, 7),
    Monkey([81, 89, 56, 61, 99], lambda x: x*7, 5, 1, 5),
    Monkey([97, 74, 68], lambda x: x+1, 17, 2, 5),
    Monkey([78, 73], lambda x: x+3, 19, 2, 3),
    Monkey([50], lambda x: x+5, 7, 1, 6),
    Monkey([95, 88, 53, 75], lambda x: x+8, 3, 0, 7),
    Monkey([50, 77, 98, 85, 94, 56, 89], lambda x: x+2, 13, 4, 0),
]

# monkeys = [
#     Monkey([79, 98], lambda x: x*19, 23, 2, 3),
#     Monkey([54, 65, 75, 74], lambda x: x+6, 19, 2, 0),
#     Monkey([79, 60, 97], lambda x: x*x, 13, 1, 3),
#     Monkey([74], lambda x: x+3, 17, 0, 1),
# ]


for i in range(20):
    for m in monkeys:
        m.inspect(monkeys)

inspections = sorted([m.inspections for m in monkeys])
print(inspections[-1]*inspections[-2])
