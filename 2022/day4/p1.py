def range_in_range(r1, r2):
    return r1[0] >= r2[0] and r1[1] <= r2[1]

def overlap(r1, r2):
    r1 = set(range(r1[0], r1[1]+1))
    r2 = set(range(r2[0], r2[1]+1))

    return len(r1 & r2) != 0

def fullycontain(r1, r2):
    return range_in_range(r1, r2) or range_in_range(r2, r1)

input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

input = open('input.txt').read()

count = 0
count_overlap = 0

for l in input.split("\n"):
    if not l:
        continue
    r1s, r2s = l.split(',')
    r1 = [int(i) for i in r1s.split('-')]
    r2 = [int(i) for i in r2s.split('-')]

    if overlap(r1, r2):
        count_overlap += 1

    if fullycontain(r1, r2):
        count += 1

print(count)
print(count_overlap)
