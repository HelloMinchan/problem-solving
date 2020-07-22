import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

memoization = [1] + [0] * k

for i in range(n):
    for j in range(coins[i], k + 1):
        if j >= coins[i]:
            memoization[j] += memoization[j - coins[i]]

print(memoization[-1])
