from collections import deque
import sys

input = sys.stdin.readline

def bfs(dq):
    while dq:
        i, j = dq.popleft()

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]
        
            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if adj_matrix[ii][jj] and not visit[ii][jj]:
                visit[ii][jj] = True
                dq.append((ii,jj))

T = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(T):
    M, N, K = map(int, input().split())

    answer = 0
    adj_matrix = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        j, i = map(int, input().split())

        adj_matrix[i][j] = 1
    
    dq = deque()
    
    for i in range(N):
        for j in range(M):
            if adj_matrix[i][j] and not visit[i][j]:
                answer += 1
                visit[i][j] = True
                dq.append((i,j))

                bfs(dq)
    
    print(answer)