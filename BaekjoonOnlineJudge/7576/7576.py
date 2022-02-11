# 5:53 ~ 6:09 (16분)
from collections import deque
import sys

input = sys.stdin.readline


def bfs(dq):
    global answer, unriped_tomatos

    while dq:
        answer += 1

        for _ in range(len(dq)):
            i, j = dq.popleft()

            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                    continue

                if box[ii][jj] == "0" and not visit[ii][jj]:
                    visit[ii][jj] = True
                    unriped_tomatos -= 1

                    dq.append((ii, jj))


answer = -1
M, N = map(int, input().split())

box = [list(input().split()) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
unriped_tomatos = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dq = deque()

for i in range(N):
    for j in range(M):
        if box[i][j] == "0":
            unriped_tomatos += 1
        elif box[i][j] == "1":
            visit[i][j] = True
            dq.append((i, j))

bfs(dq)


if unriped_tomatos:
    print(-1)
else:
    print(answer)