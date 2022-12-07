COL_A = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

COL_B = {
    'X': 'R',
    'Y': 'P',
    'Z': 'S'
}

BATTLE_WIN = [
    ('R', 'S'),
    ('P', 'R'),
    ('S', 'P'),
]

SCORE_ELEMENT = {
    'R': 1,
    'P': 2,
    'S': 3,
}

def score(ta, tb):
    a = COL_A[ta]
    b = COL_B[tb]

    s = SCORE_ELEMENT[b]

    if a == b:
        bs = 3
    elif (b, a) in BATTLE_WIN:
        bs = 6
    else:
        bs = 0

    print([ta, tb, a, b, s, bs, s+bs])

    return s + bs


input = """A Y
B X
C Z"""

input = open('input.txt').read()

s = 0
for l in input.split("\n"):
    if not l:
        continue

    a, b = l.split(" ")
    s += score(a, b)

print(s)

