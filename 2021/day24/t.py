lines = [l.strip() for l in open('input.txt').read().splitlines()]
for i in lines:
    if 'inp' in i:
        print()

    print(i, end=",")
