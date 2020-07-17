import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cost = [int(input()) for _ in range(N)]

count = 0

for i in range(N - 1, -1, -1):
    temp = K // cost[i]

    count += temp

    K -= cost[i] * temp

print(count)
