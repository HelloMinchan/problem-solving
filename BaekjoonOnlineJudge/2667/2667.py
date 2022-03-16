from collections import deque
import sys

input = sys.stdin.readline

def bfs(dq):
    count = 0

    while dq:
        i, j = dq.popleft()
        count += 1

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N-1 or jj < 0 or jj > N-1:
                continue

            if board[ii][jj] == "1" and not visit[ii][jj]:
                visit[ii][jj] = True
                dq.append((ii,jj))

    answer_list.append(count)

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

answer_list = []

for i in range(N):
    for j in range(N):
        if board[i][j] == "1" and not visit[i][j]:
            visit[i][j] = True
            dq = deque()
            dq.append((i,j))
            bfs(dq)

print(len(answer_list))

for answer in sorted(answer_list):
    print(answer)