from collections import deque
import sys
input = sys.stdin.readline


def moveHorse(dq, x, y, horse):
    for horseWay in range(8):
        xx = x + horseX[horseWay]
        yy = y + horseY[horseWay]

        if xx < 0 or xx > H - 1 or yy < 0 or yy > W - 1:
            continue
        
        if not visit[horse + 1][xx][yy] and not grid[xx][yy]:
            visit[horse + 1][xx][yy] = True
            dq.append((xx, yy, horse + 1))


def BFS(x, y):
    count = 0
    dq = deque()
    dq.append((x, y, 0))

    while dq:
        dqSize = len(dq)

        for _ in range(dqSize):
            i, j, horse = dq.popleft()

            if i == H - 1 and j == W - 1:
                return count
                
            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > H - 1 or jj < 0 or jj > W - 1:
                    continue
                
                if horse < K:
                    moveHorse(dq, i, j, horse)
                
                if not visit[horse][ii][jj] and not grid[ii][jj]:
                    visit[horse][ii][jj] = True
                    dq.append((ii, jj, horse))

        count += 1

    return -1


K = int(input())
W, H = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(H)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
horseX, horseY = [-1, -1, 1, 1, -2, -2, 2, 2], [-2, 2, -2, 2, -1, 1, -1, 1]
visit = [[[False] * W for _ in range(H)] for _ in range(K + 1)]

visit[0][0][0] = True
print(BFS(0, 0))
