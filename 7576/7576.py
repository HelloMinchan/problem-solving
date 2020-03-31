from collections import deque
import sys
input = sys.stdin.readline


def BFS(ripedTomato):
    global tomatos, visit, dx, dy, days
    dq = deque()

    for tomato in ripedTomato:
        i, j = tomato
        dq.append((i, j))
    
    while len(dq):
        for i in range(len(dq)):
            x, y = dq.popleft()

            if not visit[x][y]:
                visit[x][y] = True
                if not tomatos[x][y]:
                    tomatos[x][y] = 1

                for way in range(4):
                    ii, jj = x + dx[way], y + dy[way]
                    
                    if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1 or tomatos[ii][jj] == -1:
                        continue

                    dq.append((ii, jj))
                    
        days += 1


M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
days = 0
ripedTomato = []

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            ripedTomato.append((i, j))

BFS(ripedTomato)

for tomatoLine in tomatos:
    if tomatoLine.count(0):
        print(-1)
        exit()
if days == 1:
    print(days - 1)
else:
    print(days - 2)