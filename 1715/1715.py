import sys, heapq
input = sys.stdin.readline

N = int(input())
hq = []
minCompareCount = 0

for _ in range(N):
    heapq.heappush(hq, int(input()))

for _ in range(N - 1):
    compareCountA = heapq.heappop(hq)
    compareCountB = heapq.heappop(hq)

    heapq.heappush(hq, compareCountA + compareCountB)
    minCompareCount += compareCountA + compareCountB
    
print(minCompareCount)