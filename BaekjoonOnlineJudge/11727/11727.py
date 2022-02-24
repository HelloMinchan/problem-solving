# 1:26 ~ 1:32 (6분)

import sys

input = sys.stdin.readline

n = int(input())

dp_table = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1:
        dp_table[i] = 1
    elif i == 2:
        dp_table[i] = 3
    else:
        dp_table[i] = (dp_table[i - 1] + (dp_table[i - 2] * 2)) % 10007

print(dp_table[-1])
