import os
from collections import defaultdict

pwd = os.path.dirname(__file__)

input = open(pwd+'/input.txt').read().strip()

template, rules_raw = input.split("\n\n")
LAST_CHAR = template[-1]

def polymer_from_template(template):
    polymer = defaultdict(int)
    for i in range(len(template)-1):
        key = template[i:i+2]
        polymer[key] += 1
    return polymer

def count_chars(polymer):
    chars = defaultdict(int)
    for key, num in polymer.items():
        chars[key[0]] += num
    chars[LAST_CHAR] += 1
    return chars

rules = {}
for line in rules_raw.split("\n"):
    key, insert = line.split(' -> ')
    rules[key] = [key[0]+insert, insert+key[1]]

polymer = polymer_from_template(template)

for _ in range(40):
    new_polymer = defaultdict(int)
    for key, num in polymer.items():
        if key in rules:
            for new_key in rules[key]:
                new_polymer[new_key] += num
        else:
            new_polymer[key] = num
    polymer = new_polymer

count = count_chars(polymer)
print(max(count.values())-min(count.values()))
