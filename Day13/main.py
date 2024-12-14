import sys
import re
from enum import Enum
import numpy as np

io = sys.stdin
lines = []
for line in io:
    lines.append(line.strip())

i = 0
sum = 0
while i < len(lines):
    a_match = re.match(r'Button A: X\+([0-9]+), Y\+([0-9]+)', lines[i])
    a_x = np.int64(a_match.group(1))
    a_y = np.int64(a_match.group(2))

    i += 1

    b_match = re.match(r'Button B: X\+([0-9]+), Y\+([0-9]+)', lines[i])
    b_x = np.int64(b_match.group(1))
    b_y = np.int64(b_match.group(2))

    i += 1

    prize_match = re.match(r'Prize: X\=([0-9]+), Y\=([0-9]+)', lines[i])
    prize_x = int(prize_match.group(1))
    prize_y = int(prize_match.group(2))
    # prize_x = np.int64(10000000000000)+np.int64(prize_match.group(1))
    # prize_y = np.int64(10000000000000)+np.int64(prize_match.group(2))

    if a_x / b_x == a_y / b_y:
        print("oops")

    a = np.array([[a_x, b_x], [a_y, b_y]], dtype=np.int64)
    b = np.array([prize_x, prize_y], dtype=np.int64)
    x = np.linalg.solve(a,b)

    if np.round(x[0]) >= 0 and np.round(x[1]) >= 0:
        if np.round(x[0]) * a_x + np.round(x[1]) * b_x == prize_x and np.round(x[0]) * a_y + np.round(x[1]) * b_y == prize_y:
            sum += 3*np.round(x[0]) + np.round(x[1])

    i += 2
    
print(int(sum))