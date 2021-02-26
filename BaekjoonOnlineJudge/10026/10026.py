from collections import deque
import sys
input = sys.stdin.readline

def BFS(i, j, color, adjacentMatrix, visit):
    dq = deque()
    dq.append((i,j))

    while dq:
        i, j = dq.popleft()
        
        visit[i][j] = True

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]
            
            if ii < 0 or ii > N-1 or jj < 0 or jj > N-1:
                continue
            
            if not visit[ii][jj] and adjacentMatrix[ii][jj] == color:
                visit[ii][jj] = True
                dq.append((ii,jj))

def getDivisionCount(adjacentMatrix):
    divisionCount = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                visit[i][j] = True
                divisionCount += 1
                BFS(i, j, adjacentMatrix[i][j], adjacentMatrix, visit)

    return divisionCount

N = int(input())
dx, dy = [0,0,-1,1], [-1,1,0,0]

adjacentMatrix = [list(input().rstrip()) for _ in range(N)]
adjacentMatrix_colorBlindness = [list("".join(row).replace("G","R")) for row in adjacentMatrix]


print(getDivisionCount(adjacentMatrix), getDivisionCount(adjacentMatrix_colorBlindness))