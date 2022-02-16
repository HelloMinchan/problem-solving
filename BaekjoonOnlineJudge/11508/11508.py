# 5:13 ~ 5:22 (9분)
import sys, heapq

input = sys.stdin.readline

N = int(input())
answer = 0
hq = []

for _ in range(N):
    heapq.heappush(hq, -int(input()))

bundle = []
while hq:
    price = -heapq.heappop(hq)

    bundle.append(price)
    if len(bundle) == 3:
        answer += sum(bundle[:2])

        bundle = []

answer += sum(bundle)

print(answer)