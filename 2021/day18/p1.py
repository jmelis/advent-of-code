from json import loads as l
from math import ceil, floor, lgamma
from copy import deepcopy
import pdb

def index_of_first(lst, pred):
    for i,v in enumerate(lst):
        if pred(v):
            return i
    return None


def add(a, b):
    return [a, b]

def magnitude(r):
    if isinstance(r, int):
        return r
    if isinstance(r[0], int):
        leftval = r[0]
    else:
        leftval = magnitude(r[0])
    if isinstance(r[1], int):
        rightval = r[1]
    else:
        rightval = magnitude(r[1])
    return 3*leftval + 2*rightval

def get_explode_numbers(n, pos=None, numbers=None):
    if numbers is None:
        numbers = []

    if pos is None:
        pos = []

    exploded = False
    if len(pos) == 4:
        explode_index = index_of_first(numbers, lambda x: x[0] == 'explode')
        if explode_index is None:
            exploded = True
            numbers.append(('explode', pos, *n))
        # return

    newpos = pos.copy() + [0]
    if isinstance(n[0], int):
        if not exploded:
            numbers.append(tuple(newpos))
    else:
        get_explode_numbers(n[0], newpos, numbers)

    newpos = pos.copy() + [1]
    if isinstance(n[1], int):
        if not exploded:
            numbers.append(tuple(newpos))
    else:
        get_explode_numbers(n[1], newpos, numbers)
    
    return numbers

def split(l):
    if isinstance(l[0], int):
        if l[0] >= 10:
            l[0] = [floor(l[0]/2), ceil(l[0]/2)]
            return True
    else:
        res = split(l[0])
        if res is True:
            return True

    if isinstance(l[1], int):
        if l[1] >= 10:
            l[1] = [floor(l[1]/2), ceil(l[1]/2)]
            return True
    else:
       res = split(l[1])
       if res is True:
           return True

    return False

def getval(l, pos, ):
    for i in pos:
        l = l[i]
    return l

def setval(l, pos, val):
    for i in pos[:-1]:
        l = l[i]
    l[pos[-1]] = val

def explode(l):
    numbers = get_explode_numbers(l)
    explode_index = index_of_first(numbers, lambda x: x[0] == 'explode')
    if explode_index is not None:
        left, right = numbers[explode_index][2:]
        pos = numbers[explode_index][1]
        setval(l, pos, 0)
        prev_explode = explode_index - 1 if explode_index > 0 else None
        if prev_explode is not None:
            pos = numbers[prev_explode]
            setval(l, pos, getval(l, pos) + left)
        post_explode = explode_index + 1 if explode_index < len(numbers) - 1 else None
        if post_explode is not None:
            pos = numbers[post_explode]
            setval(l, pos, getval(l, pos) + right)
        return True
    return False

def process(l):
    while True:
        res = explode(l) or split(l)
        if not res:
            break

input = [
[[2,[2,3]],[[[0,0],[2,2]],[[3,3],[3,5]]]],
[[[8,[8,8]],6],[9,5]],
[[[[5,2],3],[[5,8],[1,1]]],[[[4,2],3],[[1,6],4]]],
[[[[6,8],[0,9]],8],[[[9,4],6],[8,6]]],
[9,[[6,7],4]],
[[1,[3,6]],[5,[[7,4],6]]],
[[[[4,7],6],[[8,9],5]],[[[6,2],[2,7]],[[9,0],[7,0]]]],
[[[[7,3],4],[7,[7,4]]],1],
[4,[6,6]],
[[3,[3,2]],[[7,1],[[6,4],[6,1]]]],
[[[[8,7],4],8],[[[8,9],5],[6,[2,7]]]],
[[4,[3,[4,1]]],8],
[5,[[5,1],9]],
[[3,[[2,4],[3,5]]],[3,[8,6]]],
[[[1,9],[[4,0],[8,5]]],[[0,[1,0]],[5,[8,7]]]],
[[[6,6],[[5,0],[3,4]]],[[3,7],6]],
[[[[0,7],[6,3]],[[2,6],8]],[[[3,0],8],[[4,0],[6,8]]]],
[[[[0,4],[6,3]],[1,[9,1]]],[[1,[1,4]],9]],
[[[[8,3],2],[0,[6,8]]],[5,[[4,4],[1,8]]]],
[[[[1,0],[7,8]],6],[3,[[5,4],[4,2]]]],
[2,[9,5]],
[[4,[2,[0,0]]],[[1,3],[1,9]]],
[6,[[[2,6],2],9]],
[[6,[1,[7,9]]],[[[7,6],[8,8]],[1,7]]],
[[[3,7],[6,9]],[5,2]],
[[[6,1],9],[[9,7],[2,[9,1]]]],
[[[[2,9],7],[[8,1],[2,1]]],[4,[[3,0],9]]],
[[[0,0],[[8,9],[2,8]]],[[[8,4],5],[0,[1,0]]]],
[[[[6,5],[3,6]],[[6,0],[0,4]]],[[[4,1],[4,2]],[5,1]]],
[[[6,[2,9]],[0,7]],[8,[[7,7],[9,9]]]],
[3,[[7,[5,7]],[6,[9,7]]]],
[[0,[3,[9,9]]],[[3,[5,8]],[3,[6,5]]]],
[[[5,[7,1]],[[9,9],[7,0]]],[0,8]],
[[[1,[4,5]],[5,[4,6]]],[1,[[1,0],9]]],
[[[[4,2],7],[[0,6],7]],[8,[[6,8],0]]],
[9,[3,[[7,3],9]]],
[[7,6],[[1,[2,8]],[[3,2],[9,1]]]],
[[[0,5],[3,[6,6]]],[[[1,5],[1,8]],[[8,9],8]]],
[[8,[[1,6],[2,0]]],[[[3,7],3],0]],
[[[0,[6,2]],[9,[5,8]]],[[[1,1],4],[8,4]]],
[[[[3,5],[5,8]],7],[[3,6],8]],
[[5,[1,0]],[[[1,3],6],[[6,8],5]]],
[[[[7,4],0],[5,1]],[[8,7],4]],
[[3,[8,3]],[[8,[3,8]],6]],
[[1,[[0,7],[2,7]]],[[2,9],[6,[8,3]]]],
[[[5,[1,9]],[2,[7,0]]],[[[5,3],2],[1,[9,1]]]],
[[[[0,0],[0,9]],[[0,8],4]],[[7,[3,9]],4]],
[[4,0],[0,4]],
[1,[[[5,5],4],[[7,7],3]]],
[[[[0,0],[9,9]],[[9,8],[8,1]]],[[[1,4],[0,2]],[1,0]]],
[[[1,[4,0]],1],[4,[6,5]]],
[2,[[[3,3],4],[[2,9],[3,9]]]],
[[[[3,2],[2,6]],[[5,8],[1,1]]],[[[4,9],9],1]],
[[[5,[1,1]],2],[[[2,9],3],[3,4]]],
[[[0,[6,2]],[4,[3,8]]],[[[3,5],[6,5]],[[9,9],2]]],
[[[[1,2],5],[[5,2],[3,0]]],[[6,[0,1]],[[3,5],8]]],
[[2,[[5,2],[5,5]]],[3,[[1,1],2]]],
[[[[4,1],[8,8]],[[2,5],2]],[[[1,4],[3,3]],1]],
[[[1,1],[2,[3,6]]],[[[0,8],[3,1]],[[1,1],[2,6]]]],
[[0,[[5,1],5]],[1,[[0,0],7]]],
[[[4,1],[[2,7],4]],[[[8,1],[2,2]],[[3,1],[1,7]]]],
[[[1,[7,4]],[[1,8],[7,4]]],[[2,3],[7,[9,6]]]],
[[[9,6],[[6,1],5]],[[[9,2],3],[[2,4],8]]],
[[[[8,8],2],9],[5,0]],
[[[8,5],[2,1]],[8,[2,9]]],
[[[[5,3],9],2],[[[1,0],[2,4]],5]],
[[[[0,8],0],1],[[5,[4,1]],[5,2]]],
[[[[6,4],[6,2]],[3,[4,0]]],[[[9,6],8],[[6,8],[5,3]]]],
[[9,9],[1,1]],
[[0,[[9,2],1]],[[[6,4],[8,3]],6]],
[[[8,9],[4,3]],[[2,[2,7]],[[2,3],8]]],
[[[[8,4],[7,5]],[4,2]],[[[9,4],0],[[9,2],[7,9]]]],
[8,[[[6,8],3],[[5,3],5]]],
[[[[9,3],0],[1,4]],[[7,[4,7]],4]],
[[[5,[4,6]],6],[[[8,0],1],[[1,8],0]]],
[[[[0,9],[1,7]],[3,9]],[[[2,7],[5,2]],[[4,6],[7,0]]]],
[[[5,[0,5]],5],[[[8,9],2],[9,6]]],
[[6,[6,[9,0]]],[[[7,3],[5,0]],[2,[1,5]]]],
[2,[[9,6],[3,[3,7]]]],
[[[1,6],[7,1]],9],
[[[[2,4],2],[[6,1],[6,3]]],[[6,[9,7]],6]],
[[[[6,6],[2,9]],[[9,6],[3,5]]],[5,3]],
[[[[7,2],6],6],[3,[2,[8,2]]]],
[[[[6,9],[6,9]],3],[[[6,5],4],8]],
[7,[[1,8],[[2,1],5]]],
[[9,5],9],
[[[8,9],[6,4]],[[2,2],[[3,5],[9,0]]]],
[[[[2,3],8],[1,8]],[[[8,2],[3,8]],[[0,3],2]]],
[[0,[2,[1,9]]],[9,0]],
[[[[7,9],[0,8]],7],[5,[[3,8],[0,4]]]],
[[[8,9],[1,[6,0]]],[[5,3],4]],
[7,[[9,9],7]],
[[[[6,8],2],[[4,4],[4,6]]],[[1,[4,6]],[2,7]]],
[[6,2],[5,[2,1]]],
[[[6,0],[[0,9],[8,3]]],[7,[[1,1],[0,1]]]],
[[[0,[0,6]],[8,0]],0],
[[3,[[4,8],5]],[[7,3],[5,0]]],
[[6,[8,[0,2]]],2],
[[[7,2],6],3],
[[[3,[1,1]],3],[[7,9],[2,[2,3]]]],
]

# input = [
# [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]],
# [[[5,[2,8]],4],[5,[[9,9],0]]],
# [6,[[[6,2],[5,6]],[[7,6],[4,7]]]],
# [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]],
# [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]],
# [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]],
# [[[[5,4],[7,7]],8],[[8,3],8]],
# [[9,3],[[9,9],[6,[4,9]]]],
# [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]],
# [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]],
# ] 

mag = 0
for i in range(len(input)):
    for j in range(len(input)):
        if i == j:
            continue
        l = [deepcopy(input[i]), deepcopy(input[j])]
        process(l)
        mag = max(magnitude(l), mag)
print(mag)
