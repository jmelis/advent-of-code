with open('input.txt') as f:
    lines = f.readlines()

# lines = """forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2""".split("\n")

pos = 0
depth = 0
aim = 0
for line in lines:
    cmd, amount = line.split()
    amount = int(amount)
    print({"pos": pos, "depth": depth})
    if cmd == 'forward':
        pos += amount
        depth += aim * amount
    elif cmd == 'down':
        # depth += amount
        aim += amount
    elif cmd == 'up':
        # depth -= amount
        aim -= amount

print(pos*depth)
