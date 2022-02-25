# 4:45 ~ 5:02 (17분)

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)])
dp_table = [1] + [0 for _ in range(k)]


for coin in coins:
    for money in range(1, k + 1):
        if money - coin >= 0:
            if dp_table[money - coin]:
                dp_table[money] += dp_table[money - coin]

print(dp_table[k])