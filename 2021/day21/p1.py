from collections import namedtuple

def roller_gen():
    i = 2
    while True:
        yield 3*i
        i+=3

Player = namedtuple('Player', ['pos', 'score'])

class Player:
    def __init__(self, pos, score=0):
        self.pos = pos
        self.score = score

    def win(self):
        return self.score >= 1000

    def move(self, n):
        self.pos = (self.pos - 1 + n) % 10 + 1
        self.score += self.pos

p1 = Player(pos=8, score=0)
p2 = Player(pos=6, score=0)

roller = roller_gen()
rolls = 0
players = [p1, p2]
finished = False
while not finished:
    for i, p in enumerate(players):
        roll = next(roller)
        rolls += 3
        p.move(roll)
        if p.win():
            print(players[1-i].score*rolls)
            finished = True
            break

