COL_A = {
    'A': 'R',
    'B': 'P',
    'C': 'S'
}

SCORE_ELEMENT = {
    'R': 1,
    'P': 2,
    'S': 3,
}

OPTS = {
    'R': 'SRP',
    'P': 'RPS',
    'S': 'PSR',
}



def score(ta, tb):
    a = COL_A[ta]

    idx = 'XYZ'.index(tb)

    b = OPTS[a][idx]


    print([ta,tb,a,b,SCORE_ELEMENT[b], idx*3])

    return SCORE_ELEMENT[b] + idx*3


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

