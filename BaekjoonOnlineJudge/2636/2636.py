from collections import deque
import sys
input = sys.stdin.readline


def checkOutAir(x, y):
    dq = deque()
    visit[x][y] = True
    dq.append((x, y))

    while dq:
        i, j = dq.popleft()

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if plate[ii][jj] == 1:
                plate[ii][jj] = -1
            
            if not visit[ii][jj] and plate[ii][jj] == 0:
                visit[ii][jj] = True
                dq.append((ii, jj))


N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

cheeze = 0
for line in plate:
    cheeze += line.count(1)

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
hour = 0

while 1:
    visit = [[False for _ in range(M)] for _ in range(N)]

    # 바깥 공기 체크
    checkOutAir(0, 0)

    meltSize = 0

    for i in range(N):
        for j in range(M):
            if plate[i][j] == -1:
                plate[i][j] = 0
                meltSize += 1

    cheeze -= meltSize
    hour += 1

    if not cheeze:
        print(hour)
        print(meltSize)
        break
