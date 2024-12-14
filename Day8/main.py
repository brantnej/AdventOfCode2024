import sys
import math
from enum import Enum
io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

antenna_dict = {}
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != '.':
            if lines[i][j] not in antenna_dict:
                antenna_dict[lines[i][j]] = [(j, i)]
            else:
                antenna_dict[lines[i][j]].append((j, i))

y_cap = len(lines) - 1
x_cap = len(lines[0]) - 1

res = set()

for frequency in antenna_dict.values():
    for i in range(len(frequency)):
        for j in range(len(frequency)):
            if i != j:
                gcd_1 = math.gcd((frequency[i][0] - frequency[j][0]), (frequency[i][1] - frequency[j][1]))
                y_1_increment = (frequency[i][0] - frequency[j][0]) // gcd_1
                x_1_increment = (frequency[i][1] - frequency[j][1]) // gcd_1

                gcd_2 = math.gcd((frequency[j][0] - frequency[i][0]), (frequency[j][1] - frequency[i][1]))
                y_2_increment = (frequency[j][0] - frequency[i][0]) // gcd_2
                x_2_increment = (frequency[j][1] - frequency[i][1]) // gcd_2

                y_1 = frequency[i][0]
                x_1 = frequency[i][1]
                y_2 = frequency[j][0]
                x_2 = frequency[j][1]

                while (y_1 >= 0 and y_1 <= y_cap and x_1 >= 0 and x_1 <= x_cap):
                    res.add((x_1, y_1))
                    y_1 += y_1_increment 
                    x_1 += x_1_increment
                while (y_2 >= 0 and y_2 <= y_cap and x_2 >= 0 and x_2 <= x_cap):
                    res.add((x_2, y_2))
                    y_2 += y_2_increment
                    x_2 += x_2_increment

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if (i, j) in res:
            print('#', end="")
        else:
            print('.', end="")
    print("\n", end="")

print(len(res))