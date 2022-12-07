
# input ="""00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010""".split("\n")

with open('input.txt') as f:
    input = f.read().split("\n")

binlen = len(input[0])

count = [0] * binlen

for num in input:
    if len(num) != binlen:
        continue

    # import pdb; pdb.set_trace()
    for i in range(binlen):
        if num[i] == '1':
            count[i] += 1

gamma = 0
for i, val in enumerate(count):
    if val > len(input)/2:
        gamma |= 1 << (binlen-1-i)

epsilon = (2**binlen - 1) & ~gamma

print(gamma, bin(gamma))
print(epsilon, bin(epsilon))

print(gamma*epsilon)
