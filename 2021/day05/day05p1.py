input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip().split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

def gen(a, b):
    if b > a:
        return range(a, b+1)
    elif b < a:        
        return range(a, b-1, -1)
    else:
        return [a] 

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def valid(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def points(self):
        points = []
        if self.x1 == self.x2:
            for n in gen(self.y1, self.y2):
                points.append((self.x1, n))

        elif self.y1 == self.y2:
            for n in gen(self.x1, self.x2):
                points.append((n, self.y1))

        return points
    def __repr__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"
    

points = {}
for line in input:
    l, r = line.split(" -> ")
    x1, y1 = [int(i) for i in l.split(',')]
    x2, y2 = [int(i) for i in r.split(',')]
    line = Line(x1,y1,x2,y2)
    if not line.valid():
        continue

    for p in line.points():
        points.setdefault(p, 0)
        points[p]+=1

t = 0
for p, v in points.items():
    if v >= 2:
        t+=1
print(t)
