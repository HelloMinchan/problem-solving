# 11:36 ~ 12:11 (35분)
import sys

input = sys.stdin.readline

N = int(input())
stairs = [int(input()) for _ in range(N)]

dp_table = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        dp_table[i] = stairs[i]
    elif i == 1:
        dp_table[i] = stairs[i] + stairs[i - 1]
    elif i == 2:
        dp_table[i] = stairs[i] + max(stairs[i - 1], stairs[i - 2])
    else:
        dp_table[i] = stairs[i] + max(dp_table[i - 2], stairs[i - 1] + dp_table[i - 3])

print(dp_table[-1])
