import sys
input = sys.stdin.readline

N = int(input())

memoization = [[0] * 10 for _ in range(N + 1)]

for i in range(10):
    memoization[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j != 9:
            memoization[i][j] += memoization[i - 1][j + 1] % 1000000000
        if j != 0:
            memoization[i][j] += memoization[i - 1][j - 1] % 1000000000

print(sum(memoization[-1][1:]) % 1000000000)
