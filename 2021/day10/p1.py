from collections import deque
input ="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".strip().split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

chars = '()[]{}<>'

CHARS = dict(zip(chars[1::2], chars[::2]))

#p1 COST = dict(zip(chars[1::2], [3, 57, 1197, 25137]))
COST = dict(zip(chars[::2], [1,2,3,4]))

scores = []
for line in input:
    corrupted = False
    Q = deque()
    for c in line:
        if c in CHARS.values():
            Q.append(c)
        else:
            popped = Q.pop()
            if CHARS[c] != popped:
                corrupted = True
    if corrupted:
        continue

    total = 0
    while Q:
        c = Q.pop()
        total = total * 5 + COST[c]
    scores.append(total)

scores.sort()
print(scores)
print(scores[int(len(scores)/2)])

