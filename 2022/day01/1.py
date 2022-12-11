input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

input = open('7250385643.txt').read()

elves = []
c = 0
for l in input.split("\n") + [""]:
    if l:
        c += int(l)
    else:
        elves.append(c)
        c = 0

print(max(elves))
print(sum(sorted(elves)[-3:]))
