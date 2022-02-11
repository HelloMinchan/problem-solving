# 6:18 ~ 6:41 (23분)
from collections import deque
import sys

input = sys.stdin.readline


def bfs(dq):
    global answer, unreiped_tomatos

    while dq:
        answer += 1

        for _ in range(len(dq)):
            z, i, j = dq.popleft()

            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                    continue

                if boxes[z][ii][jj] == "0" and not visit[z][ii][jj]:
                    visit[z][ii][jj] = True
                    unreiped_tomatos -= 1
                    dq.append((z, ii, jj))

            for way in range(2):
                zz = z + dz[way]

                if zz < 0 or zz > H - 1:
                    continue

                if boxes[zz][i][j] == "0" and not visit[zz][i][j]:
                    visit[zz][i][j] = True
                    unreiped_tomatos -= 1
                    dq.append((zz, i, j))


answer = -1
M, N, H = map(int, input().split())
boxes = [[list(input().split()) for _ in range(N)] for _ in range(H)]
visit = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dz = [1, -1]

unreiped_tomatos = 0

dq = deque()

for z in range(H):
    for i in range(N):
        for j in range(M):
            if boxes[z][i][j] == "0":
                unreiped_tomatos += 1
            elif boxes[z][i][j] == "1":
                visit[z][i][j] = True
                dq.append((z, i, j))

bfs(dq)

if unreiped_tomatos:
    print(-1)
else:
    print(answer)