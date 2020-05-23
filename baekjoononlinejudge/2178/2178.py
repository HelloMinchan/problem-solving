from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
dq = deque()

dq.append((0, 0, 0))

while len(dq):
    i, j, moveCount = dq.popleft()
    
    if i == N - 1 and j == M - 1:
        print(moveCount + 1)
        exit()

    if not visit[i][j]:
        visit[i][j] = True

        for way in range(4):
            ii, jj = i + dx[way], j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if maze[ii][jj] == 0:
                continue

            dq.append((ii, jj, moveCount + 1))