# 6:24 ~
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    pages = [0] + list(map(int, input().split()))
    sum_stack = [0 for _ in range(K + 1)]

    for i in range(1, K + 1):
        sum_stack[i] = sum_stack[i - 1] + pages[i]

    dp_table = [[0 for i in range(K + 1)] for _ in range(K + 1)]

    for i in range(2, K + 1):
        for j in range(1, K + 2 - i):
            dp_table[j][j + i - 1] = min(
                [
                    dp_table[j][j + k] + dp_table[j + k + 1][j + i - 1]
                    for k in range(i - 1)
                ]
            ) + (sum_stack[j + i - 1] - sum_stack[j - 1])

    print(dp_table[1][K])
