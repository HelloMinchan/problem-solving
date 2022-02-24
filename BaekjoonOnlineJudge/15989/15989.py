# 7:15 ~
import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    n = int(input())

    dp_table = [0 for _ in range(n + 1)]

    dp_table[0] = 1

    for i in range(1, 4):
        for j in range(i, n + 1):
            dp_table[j] += dp_table[j - i]

    print(dp_table[-1])