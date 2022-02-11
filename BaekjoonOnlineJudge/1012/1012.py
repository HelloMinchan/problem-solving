# 4:52 ~ 5:11 (19분)
from collections import deque
import sys

input = sys.stdin.readline


def BFS(dq):
    while dq:
        i, j = dq.popleft()

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if field[ii][jj] and not visit[ii][jj]:
                visit[ii][jj] = True
                dq.append((ii, jj))


T = int(input())

for _ in range(T):
    answer = 0
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    visit = [[False for _ in range(M)] for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for _ in range(K):
        x, y = map(int, input().split())

        field[y][x] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] and not visit[i][j]:
                answer += 1
                visit[i][j] = True
                dq = deque()
                dq.append((i, j))
                BFS(dq)

    print(answer)