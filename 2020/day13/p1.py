input = """939
7,13,x,x,59,x,31,19""".split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

timestamp = int(input[0])
ids = [int(i) for i in input[1].split(',') if i != 'x']
print(timestamp)
print(ids)

mintime = None
solution = None
for busid in ids:
    remainder = timestamp % busid
    if remainder != 0:
        remainder = busid - remainder
    
    if not mintime or remainder < mintime:
        mintime = remainder
        solution = remainder * busid

print(solution)
