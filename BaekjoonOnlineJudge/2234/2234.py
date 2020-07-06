from collections import deque
import sys
input = sys.stdin.readline


def isPossible(x, y, di):
    # 서
    if di == 0:
        if castle[x][y] & (1 << 1):
            return False
        else:
            return True
    # 북
    elif di == 1:
        if castle[x][y] & (1 << 2):
            return False
        else:
            return True
    # 동
    elif di == 2:
        if castle[x][y] & (1 << 3):
            return False
        else:
            return True
    # 남
    else:
        if castle[x][y] & (1 << 4):
            return False
        else:
            return True


def BFS(i, j):
    dq = deque()
    dq.append((i, j))

    while dq:
        i, j = dq.popleft()
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > n - 1 or jj < 0 or jj < m - 1:
                continue
            
            # 벽 있는지 체크
            if isPossible(i, j, way):


n, m = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
roomNum = -1

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            visit[i][j] = roomNum
            BFS(i, j)
            roomNum -= 1
