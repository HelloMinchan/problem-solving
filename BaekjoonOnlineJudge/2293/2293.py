import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])

dp_table = [1] + [0 for _ in range(k)]

for coin in coins:
    for i in range(1, k + 1):
        if i - coin >= 0:
            dp_table[i] += dp_table[i - coin]

print(dp_table[-1])
        
