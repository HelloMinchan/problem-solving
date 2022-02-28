import sys

input = sys.stdin.readline

N, K = map(int,input().split())
dp_table = [[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1, K+1):
    dp_table[i][1] = i

for i in range(1, K+1):
    for j in range(2, N+1):
        dp_table[i][j] = dp_table[i][j-1] + dp_table[i-1][j]

print(dp_table[K][N] % 1000000000)