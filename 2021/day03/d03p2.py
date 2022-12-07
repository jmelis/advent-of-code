
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
input = [int(i, 2) for i in input if len(i) > 0]


def get_oxy_filter_bit(input, bit):
    count = 0
    for i in input:
        if i & (1 << bit):
            count += 1
    return 0 if count < len(input)/2 else 1

def get_co2_filter_bit(input, bit):
    count = 0
    for i in input:
        if i & (1 << bit):
            count += 1
    return 1 if count < len(input)/2 else 0

input_oxy = input[:]
input_co2 = input[:]

oxy = 0
co2 = 0
for bit in range(binlen, 0, -1):
    bit -= 1

    oxy_filter_bit = get_oxy_filter_bit(input_oxy, bit)
    input_oxy = [i for i in input_oxy if i >> bit & 1 == oxy_filter_bit]
    if len(input_oxy) == 1:
        oxy = input_oxy[0]

    co2_filter_bit = get_co2_filter_bit(input_co2, bit)
    print(co2_filter_bit)
    input_co2 = [i for i in input_co2 if i >> bit & 1 == co2_filter_bit]
    if len(input_co2) == 1:
        co2 = input_co2[0]
    
    if oxy != 0 and co2 != 0:
        break


print(oxy)
print(co2)
print(oxy*co2)

# for num in input:
#     if len(num) != binlen:
#         continue

#     for i in range(binlen):
#         if num[i] == '1':
#             count[i] += 1

# gamma = 0
# for i, val in enumerate(count):
#     if val > len(input)/2:
#         gamma |= 1 << (binlen-1-i)

# epsilon = (2**binlen - 1) & ~gamma

# print(gamma, bin(gamma))
# print(epsilon, bin(epsilon))

# print(gamma*epsilon)
