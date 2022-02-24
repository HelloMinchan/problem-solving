from itertools import combinations
import sys

input = sys.stdin.readline


n, m = map(int, input().split())
dp_table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(i + 1):
        if i == 0 or j == 0 or j == i:
            dp_table[i][j] = 1
        else:
            dp_table[i][j] = dp_table[i - 1][j] + dp_table[i - 1][j - 1]

print(dp_table[n][m])
