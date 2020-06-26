import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

INF = 2147483647
memoization = [0] + [INF] * (k)

for i in range(n):
    for j in range(coins[i], k + 1):
        memoization[j] = min(memoization[j], memoization[j - coins[i]] + 1)
        if not j % coins[i]:
            memoization[j] = min(memoization[j], j // coins[i])

if memoization[-1] == INF:
    print(-1)
else:
    print(memoization[-1])
