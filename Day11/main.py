import sys
import math
from enum import Enum

io = sys.stdin
nums = []
for line in io:
    nums = [int(x) for x in line.strip().split(" ")]

num_dict = {}

def add_to_dict(num, stones, dict):
    if num in dict:
        dict[num] = dict[num] + stones
    else:
        dict[num] = stones

for num in nums:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] = num_dict[num] + 1

for i in range(75):
    new_dict = {}
    for key in num_dict:
        stones = num_dict[key]
        if key == 0:
            add_to_dict(1, stones, new_dict)
        elif len(str(key)) % 2 == 0:
            midpoint = len(str(key)) // 2
            key_1 = int(str(key)[:midpoint])
            key_2 = int(str(key)[midpoint:])
            add_to_dict(key_1, stones, new_dict)
            add_to_dict(key_2, stones, new_dict)
        else:
           add_to_dict(key * 2024, stones, new_dict)
    num_dict = new_dict

print(sum([num_dict[x] for x in num_dict]))