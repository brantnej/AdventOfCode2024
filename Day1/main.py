import sys
import re
io = sys.stdin
lines = []
for line in io:
    lines.append(line)

list1 = []
list2 = []
my_dict = dict()
for line in lines:
    x = re.match('([0-9]+)(?:\\s+)([0-9]+)', line)
    num1 = int(x.group(1))
    num2 = int(x.group(2))
    list1.append(num1)
    list2.append(num2)
    if num2 in my_dict:
        my_dict[num2] += 1
    else:
        my_dict[num2] = 1
list1.sort()
list2.sort()
print(sum([abs(a - b) for a, b in zip(list1, list2)]))
print(sum([i * my_dict[i] for i in list1 if i in my_dict]))