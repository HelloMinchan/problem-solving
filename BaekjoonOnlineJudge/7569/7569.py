from collections import deque
import sys
input = sys.stdin.readline


def BFS(dq):
    global unripeCount

    day = 0

    while dq:
        dqSize = len(dq)
        day += 1

        for _ in range(dqSize):
            i, j, k = dq.popleft()

            for way in range(2):
                ii = i + dz[way]

                if ii < 0 or ii > H - 1:
                    continue

                if not visit[ii][j][k] and tomatos[ii][j][k] != -1:
                    visit[ii][j][k] = True
                    unripeCount -= 1
                    dq.append((ii, j, k))
            
            for way in range(4):
                jj = j + dx[way]
                kk = k + dy[way]

                if jj < 0 or jj > N - 1 or kk < 0 or kk > M - 1:
                    continue

                if not visit[i][jj][kk] and tomatos[i][jj][kk] != -1:
                    visit[i][jj][kk] = True
                    unripeCount -= 1
                    dq.append((i, jj, kk))
    
    if not unripeCount:
        return day - 1
    else:
        return -1


M, N, H = map(int, input().split())

tomatos = []
unripeCount = 0
start = []
visit = [[[False] * M for _ in range(N)] for _ in range(H)]
dx, dy, dz = [0, 0, -1, 1], [-1, 1, 0, 0], [-1, 1]

for i in range(H):
    floor = []
    for j in range(N):
        floor.append(list(map(int, input().split())))
    tomatos.append(floor)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomatos[i][j][k] == 1:
                visit[i][j][k] = True
                start.append((i, j, k))
            elif tomatos[i][j][k] == 0:
                unripeCount += 1

dq = deque()
for i, j, k in start:
    dq.append((i, j, k))

print(BFS(dq))

