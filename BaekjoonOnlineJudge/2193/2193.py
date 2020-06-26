import sys
input = sys.stdin.readline

N = int(input())

memoization = [[0] * 2 for _ in range(N + 1)]

memoization[1][0] = 1
memoization[1][1] = 1

for i in range(2, N + 1):
    for j in range(2):
        for k in range(2):
            if j:
                memoization[i][j] += memoization[i - 1][k]
                break
            memoization[i][j] += memoization[i - 1][k]

print(memoization[-1][1])
