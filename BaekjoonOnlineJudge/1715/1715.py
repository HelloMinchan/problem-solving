import sys, heapq
input = sys.stdin.readline

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)

answer = 0

if N == 1:
    answer = 0
else:
    while 1:
        c1 = heapq.heappop(cards)
        c2 = heapq.heappop(cards)

        comb = c1 + c2
        answer += comb

        heapq.heappush(cards, comb)

        if len(cards) == 1:
            break

print(answer)

