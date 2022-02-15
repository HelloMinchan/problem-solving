# 10:57 ~ 11:11 (14분)
import sys

input = sys.stdin.readline

N = int(input())

dp_table = [-1 for _ in range(N + 1)]

for i in range(3, N + 1):
    if i == 3:
        dp_table[i] = 1
    elif i == 5:
        dp_table[i] = 1
    else:
        if dp_table[i - 5] != -1 and dp_table[i - 3] != -1:
            dp_table[i] = min(dp_table[i - 5] + 1, dp_table[i - 3] + 1)
        elif dp_table[i - 5] != -1:
            dp_table[i] = dp_table[i - 5] + 1
        elif dp_table[i - 3] != -1:
            dp_table[i] = dp_table[i - 3] + 1

print(dp_table[-1])
