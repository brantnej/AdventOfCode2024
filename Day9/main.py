import sys
import math
from enum import Enum
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

input = [int(x) for x in lines[0]]

nums = []
file = True
index = 0
id = 0
for num in input:
    if file:
        if num != 0:
            nums.append((str(id), index, index + num - 1))
            id += 1
        file = False
    else:
        if num != 0:
            nums.append((".", index, index + num - 1))
        file = True
    index += num


res = []

moved = set()

while len(nums) > 0:
    elem = nums[-1]
    if elem[0] != '.' and elem[0] not in moved:
        moved.add(elem[0])
        size = elem[2] - elem[1] + 1
        found = False
        for i in range(len(nums)):
            candidate = nums[i]
            if candidate[0] == '.' and candidate[2] - candidate[1] + 1 >= size:
                found = True
                if candidate[2] - candidate[1] + 1 == size:
                    nums[i] = (elem[0], candidate[1], candidate[2])
                if candidate[2] - candidate[1] + 1 > size:
                    nums[i] = ('.', candidate[1] + size, candidate[2])
                    nums.insert(i, (elem[0], candidate[1], candidate[1] + size - 1))
                nums = nums[:-1]
                break
        if not found:
            res.append(elem)
            nums = nums[:-1]
    else:
        if elem[0] in moved:
            res.append(elem)
        nums = nums[:-1]

result = 0
for file in res:
    result += sum([int(file[0]) * i for i in range(file[1], file[2] + 1)])

print(result)