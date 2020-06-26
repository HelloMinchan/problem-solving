import sys
input = sys.stdin.readline

N = int(input())
memoization = [[0] * 10 for _ in range(N + 1)]

for i in range(10):
    memoization[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j + 1):
            memoization[i][j] += memoization[i - 1][k]

print(sum(memoization[-1]) % 10007)
