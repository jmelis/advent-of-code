input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def prio(c):
    oc = ord(c)
    if 97 <= oc <= 122:
        return oc - 96
    else:
        return oc - 64 + 26


score = 0
# for l in open('input.txt').read().split("\n"):
for l in input.split("\n"):
    csize = len(l)//2
    c1 = l[:csize]
    c2 = l[csize:]

    c1 = set([i for i in c1])
    c2 = set([i for i in c2])

    for i in c1&c2:
        score += prio(i)

print(score)
