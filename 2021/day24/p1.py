
class Program:
    w = 0
    x = 0
    y = 0
    z = 0

    def set(self, var, value):
        setattr(self, var, value)

    def get(self, var):
        return getattr(self, var)

    def getb(self, b):
        if b[0] == '-' or b.isnumeric():
            return int(b)
        else:
            return getattr(self, b)

    def inp(self, var):
        self.set(var, next(self.inpgen))


    def run(self, initval, instructions):
        self.w = 0
        self.x = 0
        self.y = 0
        self.z = 0

        initval = str(initval)
        def inpgenfunc():
            for i in range(len(initval)):
                yield int(initval[i])

        self.inpgen = inpgenfunc()

        for instruction in instructions.splitlines():
            if not instruction:
                continue
            chunks = instruction.split()
            func = getattr(self, chunks[0])
            func(*chunks[1:])
            print([instruction, self.w, self.x, self.y, self.z])


    def add(self, a, b):
        aval = getattr(self, a)
        bval = self.getb(b)
        result = aval + bval
        setattr(self, a, result)

    def mul(self, a, b):
        aval = getattr(self, a)
        bval = self.getb(b)
        result = aval * bval
        setattr(self, a, result)

    def div(self, a, b):
        aval = getattr(self, a)
        bval = self.getb(b)
        if bval != 0:
            result = aval // bval
            setattr(self, a, result)

    def mod(self, a, b):
        aval = getattr(self, a)
        bval = self.getb(b)
        if aval >= 0 and bval > 0:
            result = aval % bval
            setattr(self, a, result)

    def eql(self, a, b):
        aval = getattr(self, a)
        bval = self.getb(b)

        if aval == bval:
            result = 1
        else:
            result = 0

        setattr(self, a, result)

p = Program()

input = open('input.txt').read()

v = 99999999999999
while True:
    if '0' not in str(v):
        p.run(v, input)
        break
        if p.z == 257131363:
            print(p.z)
            break
    v -= 1
