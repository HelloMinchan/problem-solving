from collections import deque
import sys
input = sys.stdin.readline


def BFS(x, y):
    count = 1
    dq = deque()
    dq.append((x, y))

    while dq:
        i, j = dq.popleft()
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if bluePrint[ii][jj] == 1:
                bluePrint[ii][jj] = -1
                count += 1
                dq.append((ii, jj))

    return count


N, M, K = map(int, input().split())
coords = [tuple(map(int, input().split())) for _ in range(K)]
bluePrint = [[1 for _ in range(M)] for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

for coord in coords:
    x1, y1, x2, y2 = coord
    
    for i in range(N - y2, N - y1):
        for j in range(x1, x2):
            bluePrint[i][j] = 0

divisionList = []
for i in range(N):
    for j in range(M):
        if bluePrint[i][j] == 1:
            bluePrint[i][j] = -1
            divisionList.append(BFS(i, j))

divisionList.sort()

print(len(divisionList))
print(*divisionList)
