import sys
import os

class Ropes:
    def __init__(self, knots):
        self.knots = [(0,0)]*knots
        self.tail_visited = set([(0,0)])

    def move(self, direction, steps):
        for _ in range(steps):
            # first: move head
            prevpos = self.knots[0]
            self.knots[0] = self.move_direction(direction, prevpos)

            for i in range(1, len(self.knots)):
                if self.touching(self.knots[i], self.knots[i-1]):
                    break

                self.knots[i] = self.chase(self.knots[i-1], self.knots[i])

            self.tail_visited.add(self.knots[-1])

    @staticmethod
    def chase(head, tail):
        hx, hy = head
        tx, ty = tail

        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1

        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1

        return (tx, ty)

    def move_direction(self, direction, pos):
        match direction:
            case 'U':
                return (pos[0]+1, pos[1])
            case 'R':
                return (pos[0], pos[1]+1)
            case 'D':
                return (pos[0]-1, pos[1])
            case 'L':
                return (pos[0], pos[1]-1)

    def touching(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1

    def positions(self):
        return len(set(self.tail_visited))

    def render(self):
        for x in range(10,-10,-1):
            for y in range(-10, 10):
                if (x, y) in self.knots:
                    idx = self.knots.index((x, y))
                    if idx == 0:
                        label = "H"
                    else:
                        label = str(idx)
                    sys.stdout.write(label)
                else:
                    sys.stdout.write(".")
            print()


data = open('input.txt').read().strip().split("\n")

ropes = Ropes(10)

for l in data:
    direction, steps = l.split(" ")
    steps = int(steps)

    ropes.move(direction, steps)
    # os.system('clear')
    # ropes.render()
    # input()

print(len(ropes.tail_visited))

