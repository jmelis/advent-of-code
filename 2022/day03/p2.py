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


current = set()
score = 0
for i, l in enumerate(open('input.txt').read().split("\n")):
# for i, l in enumerate(input.split("\n")):
    if not current:
        current = set([j for j in l])
    else:
        current = current & set([j for j in l])

    if (i+1) % 3 == 0:
        for e in current:
            score += prio(e)
        current = set()

    # csize = len(l)//2
    # c1 = l[:csize]
    # c2 = l[csize:]

    # c1 = set([i for i in c1])
    # c2 = set([i for i in c2])

    # for i in c1&c2:
    #     score += prio(i)

print(score)
