def compare(a, b, level=0):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True
        elif b < a:
            return False
        return None

    if not isinstance(a, list):
        a = [a]

    if not isinstance(b, list):
        b = [b]

    for i in range(max(len(a), len(b))):
        try:
            ai = a[i]
        except IndexError:
            return True

        try:
            bi = b[i]
        except IndexError:
            return False

        c = compare(ai, bi, level+1)

        if c is not None:
            return c

data = open('input.txt').read().strip()
pairs = data.split("\n\n")
total_sum = 0
for i, pair in enumerate(pairs):
    a, b = pair.split("\n")

    a = eval(a)
    b = eval(b)

    c = compare(a,b)
    print("pair", i+1)
    print("a:", a)
    print("b:", b)
    print("compare:", c)
    if c:
        total_sum += i+1

    print()

print(total_sum)
# a = [1,1,3,1,1]
# b = [1,1,5,1,1]

# print(compare(a,b))
