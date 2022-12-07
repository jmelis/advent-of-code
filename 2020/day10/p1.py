from functools import lru_cache

with open('input.txt') as f:
    input = f.read().strip().split("\n")

# input = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3""".strip().split("\n")

adapters = [int(i) for i in input]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()

print(adapters)

@lru_cache(maxsize=None)
def ways(adapters):
    if len(adapters) == 1:
        return 1

    n = 0
    v = adapters[0]

    for i in range(min(len(adapters[1:]),3)):
        if adapters[i+1] - v <= 3:
            n += ways(adapters[i+1:])
    
    return n

print(ways(tuple(adapters)))
