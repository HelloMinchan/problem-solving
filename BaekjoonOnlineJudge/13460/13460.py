import sys, copy, heapq

input = sys.stdin.readline


def gravity(i, j, di, dj):
    move = 0
    while board[i + di][j + dj] != "#" and board[i][j] != "O":
        i += di
        j += dj
        move += 1

    return i, j, move


def BFS():
    while hq:
        count, ri, rj, bi, bj = heapq.heappop(hq)

        if count > 10:
            break

        for way in range(4):
            rii, rjj, r_move = gravity(ri, rj, dx[way], dy[way])
            bii, bjj, b_move = gravity(bi, bj, dx[way], dy[way])

            if board[bii][bjj] == "O":
                continue

            if board[rii][rjj] == "O":
                print(count)
                sys.exit(0)

            if rii == bii and rjj == bjj:
                if r_move > b_move:
                    rii -= dx[way]
                    rjj -= dy[way]
                else:
                    bii -= dx[way]
                    bjj -= dy[way]

            if not visit[rii][rjj][bii][bjj]:
                visit[rii][rjj][bii][bjj] = True
                heapq.heappush(hq, (count + 1, rii, rjj, bii, bjj))

    print(-1)


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visit = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

hq = []

for i in range(N):
    for j in range(M):
        if board[i][j] == "R":
            ri, rj = i, j
            board[i][j] = "."
        if board[i][j] == "B":
            bi, bj = i, j
            board[i][j] = "."
        if board[i][j] == "O":
            hole = (i, j)

heapq.heappush(hq, (1, ri, rj, bi, bj))
visit[ri][rj][bi][bj] = True

BFS()