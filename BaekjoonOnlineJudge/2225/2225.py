import sys
input = sys.stdin.readline

N, K = map(int, input().split())
memoization = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(N + 1):
    memoization[1][i] = 1

for i in range(2, K + 1):
    for j in range(N + 1):
        for k in range(j + 1):
            memoization[i][j] += memoization[i - 1][k]
            memoization[i][j] %= 1000000000

print(memoization[-1][-1])
