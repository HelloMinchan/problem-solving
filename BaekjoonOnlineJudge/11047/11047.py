import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

count = 0

i = N - 1
while K:
    count += K // coins[i]
    K %= coins[i]
    i -= 1

print(count)
