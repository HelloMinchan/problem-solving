import sys, heapq
input = sys.stdin.readline

N = int(input())
maxLength = 0
maxIndex = 0
seg = [list(map(int, input().split())) + [i + 1] for i in range(N)]
seg.sort()

hq = []

for i, s in enumerate(seg):
    start = s[0]
    end = s[1]
    index = s[2]

    if not hq:
        heapq.heappush(hq, (end, index))

        if maxLength < len(hq):
            maxIndex = i
            maxLength = len(hq)
            
        continue

    while hq and hq[0][0] < start:
        heapq.heappop(hq)
    heapq.heappush(hq, (end, index))

    if maxLength < len(hq):
        maxIndex = i
        maxLength = len(hq)

print(maxLength)
hq = []
for i in range(maxIndex + 1):
    start = seg[i][0]
    end = seg[i][1]
    index = seg[i][2]

    if not hq:
        heapq.heappush(hq, (end, index))
        continue

    while hq and hq[0][0] < start:
        heapq.heappop(hq)
    heapq.heappush(hq, (end, index))

print(*(x[1] for x in hq))
