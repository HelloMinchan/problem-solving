# 4:07 ~ 4:29 (22분)
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)])

INF = 2147483647
dp_table = [INF for _ in range(M + 1)]
dp_table[0] = 0

for coin in coins:
    for money in range(coin, M + 1):
        if dp_table[money - coin] != INF:
            dp_table[money] = min(dp_table[money], dp_table[money - coin] + 1)

print(-1 if dp_table[-1] == INF else dp_table[-1])