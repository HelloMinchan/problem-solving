import sys

input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int,input().split()))

dp_table = [0 for _ in range(N + 1)]

for money in range(1, N+1):
    for i in range(1, N+1):
        if money - i >= 0:
            dp_table[money] = max(dp_table[money], P[i]+dp_table[money-i])

print(dp_table[-1])
