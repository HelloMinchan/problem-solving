# 5:26 ~

import sys

input = sys.stdin.readline


def make_case():
    for i in range(1, 31):
        for j in range(1, 31):
            if i == 1:
                dp_table[i][j] = j
            elif i == j:
                dp_table[i][j] = 1
            else:
                dp_table[i][j] = dp_table[i - 1][j - 1] + dp_table[i][j - 1]


T = int(input())
dp_table = [[0 for _ in range(31)] for _ in range(31)]

make_case()

for _ in range(T):
    N, M = map(int, input().split())

    print(dp_table[N][M])
