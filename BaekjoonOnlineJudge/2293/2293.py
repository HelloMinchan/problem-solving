import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp_table = [1] + [0 for _ in range(k)]

for coin in coins:
    for money in range(coin, k+1):
        if money - coin >= 0:
            dp_table[money] += dp_table[money - coin]

print(dp_table[-1])
