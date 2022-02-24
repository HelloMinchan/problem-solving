# 7:42 ~

import sys

input = sys.stdin.readline

C, N = map(int, input().split())
data = []

INF = 2147483647
dp_table = [INF for _ in range(C + 100)]
dp_table[0] = 0

for _ in range(N):
    data.append(list(map(int, input().split())))

data.sort()

for cost, customer in data:
    for i in range(customer, C + 100):
        dp_table[i] = min(dp_table[i], dp_table[i - customer] + cost)

print(min(dp_table[C:]))
