# 4:25 ~ 4:43 (18분)
from collections import deque
import sys

input = sys.stdin.readline


def BFS(dq):
    global count

    while dq:
        i, j = dq.popleft()
        count += 1

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > N - 1:
                continue

            if house_map[ii][jj] == "1" and not visit[ii][jj]:
                visit[ii][jj] = True
                dq.append((ii, jj))


answers = []
N = int(input())
house_map = [list(input().rstrip()) for _ in range(N)]
visit = [[False for _ in range(N)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(N):
        if house_map[i][j] == "1" and not visit[i][j]:
            count = 0
            dq = deque()
            visit[i][j] = True
            dq.append((i, j))
            BFS(dq)
            answers.append(count)

answers.sort()
print(len(answers))
for answer in answers:
    print(answer)