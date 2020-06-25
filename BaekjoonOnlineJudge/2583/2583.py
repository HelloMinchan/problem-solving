from collections import deque
import sys
input = sys.stdin.readline


def BFS(x, y, divisionNum):
    dq = deque()
    dq.append((x, y))

    count = 0

    while dq:
        i, j = dq.popleft()
        count += 1
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if not gridPaper[ii][jj]:
                gridPaper[ii][jj] = divisionNum
                dq.append((ii, jj))

    return count


N, M, K = map(int, input().split())
gridPaper = [[0] * (M) for _ in range(N)]
squares = [list(map(int, input().split())) for _ in range(K)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for squares in squares:
    for i in range(N - 1 - squares[1], N - squares[3] - 1, -1):
        for j in range(squares[0], squares[2]):
            if i > N - 1 or j > M - 1:
                continue
            gridPaper[i][j] = 1

division = []
divisionNum = -1
for i in range(N):
    for j in range(M):
        if not gridPaper[i][j] < 0 and not gridPaper[i][j]:
            gridPaper[i][j] = divisionNum
            division.append(BFS(i, j, divisionNum))
            divisionNum -= 1

print(len(division))
print(*sorted(division))
