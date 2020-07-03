import sys, heapq
input = sys.stdin.readline

answer = []
N = int(input())
pst = [list(map(int, input().split())) for _ in range(N)]
xCoord = []
yCoord = []
for x1, y1, x2, y2, x3, y3 in pst:
    xt = min([x1, x2, x3]) + 1
    xb = max([x1, x2, x3]) - 1

    if xt <= xb:
        heapq.heappush(xCoord, ([xt, xb]))

    yt = min([y1, y2, y3]) + 1
    yb = max([y1, y2, y3]) - 1

    if yt <= yb:
        heapq.heappush(yCoord, ([yt, yb]))

M = int(input())
xCut = []
yCut = []
for i in range(M):
    temp = input().split()

    if temp[0] == 'x':
        heapq.heappush(xCut, ([int(temp[2]), 0, i]))
    else:
        heapq.heappush(yCut, ([int(temp[2]), 0, i]))

xLine = []
yLine = []

while xCoord:
    start, end = heapq.heappop(xCoord)

    while xCut and start > xCut[0][0]:
        while xLine and xLine[0] < xCut[0][0]:
            heapq.heappop(xLine)

        temp = heapq.heappop(xCut)
        temp[1] = len(xLine)
        answer.append(temp)

    if not xCut: break

    heapq.heappush(xLine, end)

while xCut:
    while xLine and xCut[0][0] > xLine[0]:
        heapq.heappop(xLine)

    temp = heapq.heappop(xCut)
    temp[1] = len(xLine)
    answer.append(temp)

while yCoord:
    start, end = heapq.heappop(yCoord)

    while yCut and start > yCut[0][0]:
        while yLine and yLine[0] < yCut[0][0]:
            heapq.heappop(yLine)

        temp = heapq.heappop(yCut)
        temp[1] = len(yLine)
        answer.append(temp)

    if not yCut: break
    heapq.heappush(yLine, end)

while yCut:
    while yLine and yCut[0][0] > yLine[0]:
        heapq.heappop(yLine)

    temp = heapq.heappop(yCut)
    temp[1] = len(yLine)
    answer.append(temp)

for _, count, _ in sorted(answer, key=lambda x: x[2]):
    print(count)
