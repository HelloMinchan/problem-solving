# 10:43 ~

import sys

input = sys.stdin.readline

n = int(input())

gps = [int(input()) for _ in range(n)]
dp_table = [0 for _ in range(n)]

for i in range(n):
    if i == 0:
        dp_table[i] = gps[i]
    elif i == 1:
        dp_table[i] = gps[i] + dp_table[i - 1]
    elif i == 2:
        dp_table[i] = gps[i] + max(gps[i - 1], gps[i - 2])
    else:
        dp_table[i] = gps[i] + max(gps[i - 1] + dp_table[i - 3], dp_table[i - 2])

    dp_table[i] = max(dp_table[i], dp_table[i - 1])

print(dp_table[-1])