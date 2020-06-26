from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    count = 0
    while start:
        waterSize = len(water)
        count += 1

        for _ in range(waterSize):
            i, j = water.popleft()

            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > R - 1 or jj < 0 or jj > C - 1:
                    continue

                if not visit[ii][jj] and forest[ii][jj] != 'D' and forest[ii][jj] != 'X' and (ii, jj) not in start:
                    visit[ii][jj] = True
                    water.append((ii, jj))
        
        startSize = len(start)

        for _ in range(startSize):
            x, y = start.popleft()

            for way in range(4):
                xx = x + dx[way]
                yy = y + dy[way]

                if xx < 0 or xx > R - 1 or yy < 0 or yy > C - 1:
                    continue
                
                if xx == dest[0] and yy == dest[1]:
                    return count

                if not visit2[xx][yy] and not visit[xx][yy] and forest[xx][yy] != 'X':
                    visit2[xx][yy] = True
                    start.append((xx, yy))
    
    return -1


R, C = map(int, input().split())
forest = [list(input().rstrip()) for _ in range(R)]
visit = [[False] * C for _ in range(R)]
visit2 = [[False] * C for _ in range(R)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

start = deque()
water = deque()
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'D':
            dest = (i, j)
        elif forest[i][j] == 'S':
            visit2[i][j] = True
            forest[i][j] = '.'
            start.append((i, j))
        elif forest[i][j] == '*':
            visit[i][j] = True
            water.append((i, j))

ans = BFS()
if ans == -1:
    print("KAKTUS")
else:
    print(ans)
