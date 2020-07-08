import sys, bisect
input = sys.stdin.readline

n = int(input())
coord = [list(map(int, input().split())) for _ in range(n)]

coord.sort()

answer = 2147483647
INF = 2147483647
candidate = dict()

start = 0
dist = abs(coord[0][0] - coord[1][0]) ** 2 + abs(coord[0][1] - coord[1][1]) ** 2
for i in range(1, n):
    candidate[i] = tuple((coord[i][1], coord[i][0]))
    temp = []
    for j in range(start, i):
        if start <= coord[i][0] - dist:
            temp.append(start)
            start += 1
    
    for t in temp:
        del candidate[t]
    
    yCoord = []
    for c in candidate.values():
        yCoord.append(c)
    
    minY = bisect.bisect(yCoord[:], (coord[i][1] - (dist + 1), INF))
    maxY = bisect.bisect(yCoord[:], (coord[i][1] + dist, INF))
    
    for i in range(minY, maxY):
        dist = abs(coord[i][0] - candidate[i][0]) ** 2 + abs(coord[i][1] - candidate[i][1]) ** 2
    
print(dist)
