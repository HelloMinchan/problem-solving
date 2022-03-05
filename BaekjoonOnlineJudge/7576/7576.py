from collections import deque
import sys

input = sys.stdin.readline

def bfs(dq):
    global ur_tomatos

    day = - 1

    while dq:
        day += 1
        for _ in range(len(dq)):
            i, j = dq.popleft()

            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                    continue

                if tomatos[ii][jj] == 0:
                    ur_tomatos -= 1
                    tomatos[ii][jj] = 1
                    dq.append((ii, jj))

    return day

M, N = map(int, input().split())

tomatos = [list(map(int, input().split())) for _ in range(N)]

ur_tomatos = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

dq = deque()
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            dq.append((i,j))
        elif tomatos[i][j] == 0:
            ur_tomatos += 1

answer = bfs(dq)

print(answer if ur_tomatos == 0 else -1)