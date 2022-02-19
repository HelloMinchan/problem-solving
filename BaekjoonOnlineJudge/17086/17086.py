# 0:46 ~
from collections import deque
import sys

input = sys.stdin.readline


def bfs(dq, visit):
    while dq:
        dist, i, j = dq.popleft()

        for way in range(8):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if visit[way][ii][jj] > dist and space[ii][jj] != 1:
                visit[way][ii][jj] = dist
                dq.append((dist + 1, ii, jj))
            elif space[ii][jj] == 1:
                return dist + 1


N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
INF = 2147483647
answer = 0

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

for i in range(N):
    for j in range(M):
        if space[i][j] == 0:
            visit = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(8)]

            for way in range(8):
                visit[way][i][j] = 0

            dq = deque()
            dq.append((0, i, j))

            answer = max(answer, bfs(dq, visit))

print(answer)
