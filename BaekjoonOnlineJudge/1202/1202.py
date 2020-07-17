import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())

jew = []
bag = []

for _ in range(N):
    w, v = map(int, input().split())
    heapq.heappush(jew, (w, v))

for _ in range(K):
    w = int(input())
    heapq.heappush(bag, w)

answer = 0
possibleJew = []

while bag:
    bagWeight = heapq.heappop(bag)

    while jew and bagWeight >= jew[0][0]:
        w, v = heapq.heappop(jew)
        heapq.heappush(possibleJew, -v)
    
    if possibleJew:
        answer += -heapq.heappop(possibleJew)
    elif not jew:
        break

print(answer)
