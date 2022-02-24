# 5:29 ~ 5:46 (17분)

import sys

input = sys.stdin.readline

n = int(input())
seq = [0] + list(map(int, input().split()))

dp_table = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    dp_table[i] = seq[i]

    if dp_table[i] < dp_table[i - 1] + seq[i]:
        dp_table[i] = dp_table[i - 1] + seq[i]

print(max(dp_table[1:]))
