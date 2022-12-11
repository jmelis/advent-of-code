

class Hanoi:
    def __init__(self, numstacks, input):
        self.stacks = []
        self.input = input
        for _ in range(numstacks):
            self.stacks.append([])

        for l in input.split("\n"):
            if '[' not in l:
                break
            for i, start in enumerate(self.gen_starts(numstacks)):
                el = l[start+1:start+2].strip()
                if el:
                    self.stacks[i].append(el)

        for i in self.stacks:
            i.reverse()

    @staticmethod
    def gen_starts(n):
        index = 0
        for _ in range(n):
            yield index
            index += 4

    def inspect(self):
        for i in self.stacks:
            print(i)

    def run(self):
        for l in self.input.split("\n"):
            chunks = l.split()

            if len(chunks) == 0 or chunks[0] != 'move':
                continue

            n = int(chunks[1])
            source = int(chunks[3])
            target = int(chunks[5])

            self.move(n, source, target)


    def move_p1(self, n, source, target):
        source = source - 1
        target = target - 1

        for _ in range(n):
            el = self.stacks[source].pop()
            self.stacks[target].append(el)

    def move(self, n, source, target):
        source = source - 1
        target = target - 1

        tail = self.stacks[source][-n:]
        self.stacks[source] = self.stacks[source][:-n]
        self.stacks[target].extend(tail)

    def message(self):
        msg = ""
        for s in self.stacks:
            msg += s[-1]
        return msg



input = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

input = open('input.txt').read()

h = Hanoi(9,input)
h.run()
# h.inspect()
print(h.message())

# for l in input.split("\n"):
#     print(len(l))


# l = "[Z] [M] [P]" # [0:3] [4:7] [8:11]

# for start in [0,4,8]:
#     end = start + 3
#     print(l[start:end])

