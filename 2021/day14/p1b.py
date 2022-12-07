import os
from collections import defaultdict

pwd = os.path.dirname(__file__)

input = open(pwd+'/ex1').read().strip()

polymer, rules_raw = input.split("\n\n")

rules = {}
for line in rules_raw.split("\n"):
    key, insert = line.split(' -> ')
    rules[key] = insert

for step in range(10):
    new_polymer = polymer[0]
    for i in range(1, len(polymer)):
        key = polymer[i-1] + polymer[i]
        if key in rules:
            new_polymer += rules[key]
        new_polymer += polymer[i]
    polymer = new_polymer

chars = defaultdict(int)
for c in polymer:
    chars[c] += 1

print(max(chars.values())-min(chars.values()))
