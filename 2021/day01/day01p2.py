with open('input.txt') as f:
    input = f.read().split()
input = [int(i) for i in input]

# input = [
# 199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263,
# ]

def sum_n(l, index, n):
    sum = 0
    for i in range(n):
        if index - 1 >= 0:
            sum += l[index-i]
    return sum

sums = [sum_n(input, i, 3) for i in range(len(input))][2:]

input = sums
count = 0
last = None
for i in input:
    if last and i > last:
        count += 1
    last = i

print(count)
