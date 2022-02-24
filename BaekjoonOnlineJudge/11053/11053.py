# 4:14 ~ 4:29 (15분)

import sys

input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))

dp_table = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i):
        if A[i] > A[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(max(dp_table))
