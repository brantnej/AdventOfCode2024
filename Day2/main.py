import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line)

sum = 0
for line in lines:
    line_nums = [int(x) for x in line.split()]
    for i in range(len(line_nums)):
        nums = [line_nums[j] for j in range(len(line_nums)) if j != i]
        last_num = nums[0]
        increasing = nums[1] > nums[0]
        safe = True
        for i in range(1, len(nums)):
            removed_number = False
            if increasing and not(nums[i] >= last_num+1 and nums[i] <= last_num+3):
                    safe = False
                    break
            if not increasing and not(nums[i] >= last_num-3 and nums[i] <= last_num-1):
                    safe = False
                    break
            last_num = nums[i]
        if safe:
            sum += 1
            break
print(sum)
        