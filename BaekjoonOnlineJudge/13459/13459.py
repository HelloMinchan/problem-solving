from collections import deque
import sys
input = sys.stdin.readline


def gravity(x, y, dx, dy):
    count = 0

    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1

    return x, y, count


def BFS(red, blue):
    dq = deque()
    visit[red[0]][red[1]][blue[0]][blue[1]] = True
    dq.append((red[0], red[1], blue[0], blue[1], 1))

    while dq:
        ri, rj, bi, bj, count = dq.popleft()

        if count > 10:
            return False
        
        for way in range(4):
            rii, rjj, rCount = gravity(ri, rj, dx[way], dy[way])
            bii, bjj, bCount = gravity(bi, bj, dx[way], dy[way])

            if board[bii][bjj] == 'O':
                continue
            if board[rii][rjj] == 'O':
                return True
            
            if rii == bii and rjj == bjj:
                if rCount > bCount:
                    rii -= dx[way]
                    rjj -= dy[way]
                else:
                    bii -= dx[way]
                    bjj -= dy[way]
            
            if not visit[rii][rjj][bii][bjj]:
                visit[rii][rjj][bii][bjj] = True
                dq.append((rii, rjj, bii, bjj, count + 1))
    
    return False


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

hole = []
red = []
blue = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'O':
            hole.append(i)
            hole.append(j)
        elif board[i][j] == 'R':
            red.append(i)
            red.append(j)
        elif board[i][j] == 'B':
            blue.append(i)
            blue.append(j)

print(1 if BFS(red, blue) else 0)
