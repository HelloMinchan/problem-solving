# 3:22 ~ 4:30 (52분)
import sys

input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

answer = 0
cur_city = 0

while 1:
    if cur_city == N - 1:
        break

    if prices[cur_city] < prices[cur_city + 1]:
        now_city = cur_city
        while cur_city + 1 < N - 1 and prices[now_city] < prices[cur_city + 1]:
            cur_city += 1

        cur_city += 1
        answer += prices[now_city] * sum(dists[now_city:cur_city])

    else:
        answer += prices[cur_city] * dists[cur_city]
        cur_city += 1


print(answer)