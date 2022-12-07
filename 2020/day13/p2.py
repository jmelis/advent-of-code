import timeit

def naive_implementation(busids):
    n = 1
    while True:
        valid = True
        for v, r in busids.items():
            if (n+r) % v != 0:
                valid = False
                break
        if valid:
            return n
        n += 1

def jump_by_max_busid_implementation(busids):
    # recalculate busids to center around the bus with maxid
    bus_max = max(busids.keys())
    r_bus_max = busids[bus_max]
    busids = {busid: (r-r_bus_max) for busid, r in busids.items()}
    print(busids)
    n = int(100000000000000/bus_max)+1
    while True:
        valid = True
        ts = n*bus_max
        for v, r in busids.items():
            if (ts+r) % v != 0:
                valid = False
                break
        if valid:
            return ts-r_bus_max
        n += 1

input = "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,643,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17,13,x,x,x,x,23,x,x,x,x,x,x,x,509,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"

busids = {}
for i, busid in enumerate(input.split(',')):
    if busid == 'x':
        continue
    busids[int(busid)] = i

print(busids)
print(jump_by_max_busid_implementation(busids))
# print(naive_implementation(busids))
