from collections import deque
import sys
input = sys.stdin.readline
 
def BFS(dq, case):
    while(dq):
        i, j = dq.popleft()
 
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]
 
            if ii < 0 or ii > N-1 or jj < 0 or jj > N-1:
                continue
 
            if not visit[ii][jj] and region[ii][jj] > case:
                visit[ii][jj] = True
                dq.append((ii,jj))
 
 
N = int(input())
region = [list(map(int,input().split())) for _ in range(N)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
 
maxHeight = 0
 
for i in range(N):
    for j in range(N):
        if region[i][j] > maxHeight:
            maxHeight = region[i][j]
 
ans = [0] * maxHeight
 
for case in range(maxHeight+1):
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and case < region[i][j]:
                ans[case] += 1
                visit[i][j] = True
                dq = deque()
                dq.append((i,j))
                BFS(dq, case)
 
print(max(ans))