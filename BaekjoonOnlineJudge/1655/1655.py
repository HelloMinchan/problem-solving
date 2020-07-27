import sys, heapq
input = sys.stdin.readline

N = int(input())
maxHq = []
minHq = []

for _ in range(N):
    x = int(input())

    heapq.heappush(maxHq, -x)

    if len(maxHq) - len(minHq) >= 2:
        heapq.heappush(minHq, -heapq.heappop(maxHq))
    else:
        if maxHq and minHq and -maxHq[0] > minHq[0]:
            temp1 = -heapq.heappop(maxHq)
            temp2 = heapq.heappop(minHq)

            heapq.heappush(minHq, temp1)
            heapq.heappush(maxHq, -temp2)

    print(-maxHq[0])
