import sys
import re
from enum import Enum
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

sum = 0
for line in lines:
    [target, nums] = line.split(':')
    target = int(target.strip())
    nums = [int(x.strip()) for x in nums.split(' ') if x != '']
    results = { nums[0] }
    for i in range(1, len(nums)):
        new_set = set()
        for num in results:
            new_num = int(num * nums[i])
            if new_num <= target:
                new_set.add(new_num)
            new_num = int(num + nums[i])
            if new_num <= target:
                new_set.add(new_num)
            new_num = int(str(num) + str(nums[i]))
            if new_num <= target:
                new_set.add(new_num)
        results = new_set
    if target in results:
        sum += target

print(sum)