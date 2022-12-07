from collections import namedtuple, defaultdict, deque

def addpos(pos, n):
    return (pos - 1 + n) % 10 + 1

rolls = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

Player = namedtuple('Player',['score', 'pos'])
Game = namedtuple('Game', ['turn', 'count', 'p1', 'p2'])
g = Game(0, 1, Player(0, 8), Player(0, 6))
Q = deque()
Q.append(g)
finished = defaultdict(int)
while Q:
    turn, count, p1, p2 = Q.pop()
    p = p1 if turn == 0 else p2
    newpos = defaultdict(int)
    for mv, n in rolls.items():
        npos = addpos(p.pos, mv)
        newpos[npos] += n
    for npos, npos_count in newpos.items():
        new_score = p.score + npos
        new_count = count * npos_count
        if new_score >= 21:
            finished[turn] += new_count
        else:
            np = Player(new_score, npos)
            if turn == 0:
                p1 = np
            else:
                p2 = np
            
            ng = Game(1-turn, new_count, p1, p2)
            Q.append(ng)

print(max(finished.values()))
