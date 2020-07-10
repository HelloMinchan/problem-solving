from collections import deque
import sys
input = sys.stdin.readline


def isPossible(x, y, di):
    # 서
    if di == 0:
        if castle[x][y] & (1 << 0):
            return False
        else:
            return True
    # 북
    elif di == 1:
        if castle[x][y] & (1 << 1):
            return False
        else:
            return True
    # 동
    elif di == 2:
        if castle[x][y] & (1 << 2):
            return False
        else:
            return True
    # 남
    else:
        if castle[x][y] & (1 << 3):
            return False
        else:
            return True


def BFS(i, j):
    dq = deque()
    dq.append((i, j))
    count = 0

    while dq:
        i, j = dq.popleft()
        count += 1
        
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > n - 1 or jj < 0 or jj > m - 1:
                continue
            # 벽 있는지 체크
            if isPossible(i, j, way):
                if visit[ii][jj] == 0:
                    visit[ii][jj] = roomNum
                    dq.append((ii, jj))

    rooms[-roomNum] = count
    return count


n, m = map(int, input().split())
n, m = m, n
castle = [list(map(int, input().split())) for _ in range(n)]

rooms = [0] * 2501
visit = [[0] * m for _ in range(n)]
visit2 = [[0] * m for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
roomNum = -1
roomCount = 0
maxRoomCount = 0
sumMaxRoomCount = 0

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            roomCount += 1
            visit[i][j] = roomNum
            maxRoomCount = max(maxRoomCount, BFS(i, j))
            visit2[i][j] = rooms[-roomNum]
            roomNum -= 1
        else:
            visit2[i][j] = rooms[-visit[i][j]]

for i in range(n):
    for j in range(m):
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > n - 1 or jj < 0 or jj > m - 1:
                continue
            
            if visit[i][j] != visit[ii][jj]:
                if not isPossible(i, j, way):
                    sumMaxRoomCount = max(sumMaxRoomCount, visit2[i][j] + visit2[ii][jj])

print(roomCount)
print(maxRoomCount)
print(sumMaxRoomCount)
