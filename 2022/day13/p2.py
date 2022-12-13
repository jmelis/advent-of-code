from functools import cmp_to_key

def compare(a, b, level=0):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif b < a:
            return -1
        return None

    if not isinstance(a, list):
        a = [a]

    if not isinstance(b, list):
        b = [b]

    for i in range(max(len(a), len(b))):
        try:
            ai = a[i]
        except IndexError:
            return 1

        try:
            bi = b[i]
        except IndexError:
            return -1

        c = compare(ai, bi, level+1)

        if c is not None:
            return c

data = open('input.txt').read().strip()
pairs = data.split("\n\n")
messages = [[[2]], [[6]]]
for i, pair in enumerate(pairs):
    a, b = pair.split("\n")

    a = eval(a)
    b = eval(b)

    messages.append(a)
    messages.append(b)

messages = sorted(messages, reverse=True, key=cmp_to_key(compare))

prod = 1
for i, m in enumerate(messages):
    if m == [[2]] or m == [[6]]:
        prod *= i+1

print(prod)
