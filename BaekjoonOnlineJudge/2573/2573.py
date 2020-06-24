from collections import deque
import sys, copy
input = sys.stdin.readline


def BFS(x, y): 
    dq = deque()
    dq.append((x, y))
    
    while dq:
        melt = 0
        i, j = dq.popleft()

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue
            
            if not temp[ii][jj]:
                melt += 1
            
            if not visit[ii][jj] and temp[ii][jj]:
                visit[ii][jj] = True
                dq.append((ii, jj))
        
        arctic[i][j] = max(0, arctic[i][j] - melt)


N, M = map(int, input().split())
arctic = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
year = 0

while 1:
    temp = copy.deepcopy(arctic)
    visit = [[False] * M for _ in range(N)]
    imCount = 0
    
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and temp[i][j]:
                visit[i][j] = True
                imCount += 1
                BFS(i, j)

    if imCount >= 2:
        print(year)
        break
    elif not imCount:
        print(0)
        break
    
    year += 1
