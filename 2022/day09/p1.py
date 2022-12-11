class Ropes:
    def __init__(self):
        self.head = (0,0)
        self.head_prev = (0,0)
        self.tail = (0,0)
        self.tail_visited = [self.tail]

    def move(self, direction, steps):
        for _ in range(steps):
            self.head_prev = self.head
            self.head = self.calculate_pos(direction, self.head)

            if not self.touching():
                self.tail = self.head_prev
                self.tail_visited.append(self.tail)


    def calculate_pos(self, direction, pos):
        match direction:
            case 'U':
                return (pos[0]+1, pos[1])
            case 'R':
                return (pos[0], pos[1]+1)
            case 'D':
                return (pos[0]-1, pos[1])
            case 'L':
                return (pos[0], pos[1]-1)

    def touching(self):
        return abs(self.head[0] - self.tail[0]) <= 1 and abs(self.head[1] - self.tail[1]) <= 1


    def positions(self):
        return len(set(self.tail_visited))


input = open('input.txt').read().strip().split("\n")

ropes = Ropes()

for l in input:
    direction, steps = l.split(" ")
    steps = int(steps)

    ropes.move(direction, steps)

print(ropes.positions())
