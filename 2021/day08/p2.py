"""
  0(6)   1(2)x   2(5)x   3(5)x   4(4)x
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

5(5)x     6(6)x   7(3)x   8(7)x    9(6)
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
"""


input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".split("\n")

with open('input.txt') as f:
    input = f.read().strip().split("\n")

def sort(s):
    return "".join(sorted("".join(s)))

def build_dict(input_sets):
    segments = {}
    nums = {}

    def find_by_func(wordlen, func=None):
        if func is None:
            func = lambda x: True 
        return next(w for w in input_sets if len(w) == wordlen and func(w))

    nums[7] = find_by_func(3)
    nums[1] = find_by_func(2)
    segments['a'] = next(iter(nums[7]-nums[1]))

    nums[4] = find_by_func(4)
    nums[8] = find_by_func(7)

    nums[6] = find_by_func(6, not nums[7].issubset(w))

    segments['c'] = next(iter(nums[8] - nums[6]))
    segments['f'] = next(iter(nums[7]-set([segments['a'], segments['c']])))

    def find_3(w):
        return len(w) == 5 and nums[7].issubset(w)
    nums[3] = next(w for w in input_sets if find_3(w))

    def find_2(w):
        return len(w) == 5 and w != nums[3] and segments['f'] not in w
    nums[2] = next(w for w in input_sets if find_2(w))

    def find_5(w):
        return len(w) == 5 and w != nums[3] and w != nums[2]
    nums[5] = next(w for w in input_sets if find_5(w))

    def find_9(w):
        return len(w) == 6 and nums[4].issubset(w)
    nums[9] = next(w for w in input_sets if find_9(w))

    def find_0(w):
        return len(w) == 6 and w != nums[9] and w != nums[6]
    nums[0] = next(w for w in input_sets if find_0(w))

    return {sort(v): k for k, v in nums.items()}

total = 0
for line in input:
    input_sets = [set(w) for w in line.split(" | ")[0].split()]
    output_strs = ["".join(sorted(w)) for w in line.split(" | ")[1].split()]

    enc = build_dict(input_sets)
    output = int("".join([str(enc[w]) for w in output_strs]))
    total += output

print(total)
