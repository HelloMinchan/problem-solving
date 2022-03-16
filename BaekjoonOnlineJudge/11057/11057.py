import sys

input = sys.stdin.readline

N = int(input())

dp_table = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(10):
    dp_table[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp_table[i][j] = dp_table[i-1][j]
        else:
            dp_table[i][j] = sum(dp_table[i-1][:j+1])

print(sum(dp_table[-1]) % 10007)
