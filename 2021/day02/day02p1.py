with open('input.txt') as f:
    lines = f.readlines()

pos = 0
depth = 0
for line in lines:
    cmd, amount = line.split()
    amount = int(amount)
    if cmd == 'forward':
        pos += amount
    elif cmd == 'down':
        depth += amount
    else:
        depth -= amount

print(pos*depth)
