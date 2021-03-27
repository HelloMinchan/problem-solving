import sys

input = sys.stdin.readline

memoization = [[0 for _ in range(1001)] for _ in range(1001)]

memoization[1][1] = 1
memoization[2][1] = 1
memoization[2][2] = 1
memoization[3][1] = 1
memoization[3][2] = 2
memoization[3][3] = 1

for i in range(4, 1001):
    for j in range(2, 1001):
        memoization[i][j] = (
            memoization[i - 1][j - 1]
            + memoization[i - 2][j - 1]
            + memoization[i - 3][j - 1]
        ) % int(1e9 + 9)

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    print(memoization[n][m])
