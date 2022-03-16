import sys

input = sys.stdin.readline

N = int(input())
prices = [0] + list(map(int, input().split()))

dp_table = [0 for _ in range(N+1)]

for money in range(1, N+1):
    dp_table[money] = prices[money]

    for i in range(1, money):
        if money - i > 0:
            dp_table[money] = max(dp_table[money], prices[i] + dp_table[money - i])

print(dp_table[-1])
