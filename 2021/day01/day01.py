with open('input.txt') as f:
    input = f.read().split()
input = [int(i) for i in input]

count = 0
last = None
for i in input:
    if last and i > last:
        count += 1
    last = i

print(count)
