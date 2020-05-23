import sys, heapq
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    value = int(input())

    if not value:
        try:
            print(heapq.heappop(hq))
        except:
            print(0)
    else:
        heapq.heappush(hq, value)