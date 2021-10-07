from collections import deque
import sys
input = sys.stdin.readline

def BFS(i,j,burles):
    dq = deque()
    dq.append((i,j,burles))

    while dq:
        i, j, burles = dq.popleft()
        
        if i == n and j == m:
            if burles == k:
                return True
            else:
                return False
        
        if not visit[i][j]:
            visit[i][j] = True

            for way in range(2):
                ii = i + dx[way]
                jj = j + dy[way]
                
                if ii < 1 or ii > n or jj < 1 or jj > m:
                    continue
                
                if way:
                    dq.append((ii,jj,burles+jj))
                else:
                    dq.append((ii,jj,burles+ii))



dx = [0,1]
dy = [1,0]
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [[0 for _ in range(m+1)] for _ in range(n+1)]
    visit = [[False for _ in range(m+1)] for _ in range(n+1)]

    if BFS(1,1,0):
        print("YES")
    else:
        print("NO")