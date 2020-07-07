import sys
input = sys.stdin.readline        

n = int(input())

coord = [list(map(int, input().split())) for _ in range(n)]
xLines = []
yLines = []

for i in range(1, n):
    if coord[i][0] == coord[i - 1][0]:
        xLines.append((min(coord[i][1], coord[i - 1][1]), max(coord[i][1], coord[i - 1][1])))
    else:
        yLines.append((min(coord[i][0], coord[i - 1][0]), max(coord[i][0], coord[i - 1][0])))

if coord[0][0] == coord[-1][0]:
    xLines.append((min(coord[0][1], coord[-1][1]), max(coord[0][1], coord[-1][1])))
else:
    yLines.append((min(coord[-1][0], coord[0][0]), max(coord[-1][0], coord[0][0])))

x_hash = [0] * 1000001
y_hash = [0] * 1000001

for xLine in xLines:
    x_hash[xLine[0] + 500000] += 1
    x_hash[xLine[1] + 500000] += -1

for yLine in yLines:
    y_hash[yLine[0] + 500000] += 1
    y_hash[yLine[1] + 500000] += -1

maxX = x_hash[0]
for i in range(1000001):
    x_hash[i] += x_hash[i - 1]
    
    if maxX < x_hash[i]:
        maxX = x_hash[i]

maxY = y_hash[0]
for i in range(1000001):
    y_hash[i] += y_hash[i - 1]

    if maxY < y_hash[i]:
        maxY = y_hash[i]

print(max(maxX, maxY))
