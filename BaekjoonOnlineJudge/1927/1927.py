import sys, heapq
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    num = int(input())

    if not num:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, (num))
