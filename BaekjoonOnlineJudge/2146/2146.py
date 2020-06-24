from collections import deque
import sys
input = sys.stdin.readline


def constructBridge(x, y, islandNum):
    dq = deque()
    dq.append((x, y))

    bridgeLength = 0
    while dq:
        dqSize = len(dq)

        for _ in range(dqSize):
            i, j = dq.popleft()

            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > N - 1 or jj < 0 or jj > N - 1:
                    continue
                
                if MAP[ii][jj] != 0 and MAP[ii][jj] != islandNum and MAP[ii][jj] != 2:
                    return bridgeLength
                    
                if MAP[ii][jj] == 0:
                    MAP[ii][jj] = 2
                    dq.append((ii, jj))
            
        bridgeLength += 1    


def searchBeach(x, y, islandNum):
    dq = deque()
    dq.append((x, y))
    beach = []

    while dq:
        isBeach = False
        i, j = dq.popleft()

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]
            
            if ii < 0 or ii > N - 1 or jj < 0 or jj > N - 1:
                continue

            if MAP[ii][jj] != islandNum and MAP[ii][jj] != 0:
                MAP[ii][jj] = islandNum
                
                dq.append((ii, jj))

            if MAP[ii][jj] == 0:
                isBeach = True
        
        if isBeach:
            beach.append((i, j))

    return beach


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
islandNum = -1
islandEnd = []

for i in range(N):
    for j in range(N):
        if not MAP[i][j] < 0 and MAP[i][j] != 0:
            MAP[i][j] = islandNum
            islandEnd.append(searchBeach(i, j, islandNum))
            islandNum -= 1

minimumdist = 2147483647
minimumdIslandNum = 0
minimumX = 0
minimumY = 0

for i in range(len(islandEnd) - 1):
    for j in range(i + 1, len(islandEnd)):
        for k in range(len(islandEnd[i])):
            for o in range(len(islandEnd[j])):
                x1, y1 = islandEnd[i][k]
                x2, y2 = islandEnd[j][o]

                if minimumdist > abs(x1 - x2) + abs(y1 - y2):
                    minimumdist = abs(x1 - x2) + abs(y1 - y2)
                    minimumX = x1
                    minimumY = y1
                    minimumdIslandNum = MAP[x1][y1]

print(constructBridge(minimumX, minimumY, minimumdIslandNum))
