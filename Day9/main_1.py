import sys
import math
from enum import Enum
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

input = [int(x) for x in lines[0]]

res = []
free_spaces = []
file = True
id = 0
for num in input:
    if file:
        for i in range(num):
            res.append(str(id))
        id += 1
        file = False
    else:
        for i in range(num):
            res.append('.')
        file = True

left_idx = 0
right_idx = len(res) - 1
while left_idx < right_idx:
    if res[left_idx] == '.':
        while res[right_idx] == '.':
            right_idx -= 1
        res[left_idx] = res[right_idx]
        res[right_idx] = '.'
    left_idx += 1

print(sum([i * int(res[i]) for i in range(len(res)) if res[i] != '.']))

