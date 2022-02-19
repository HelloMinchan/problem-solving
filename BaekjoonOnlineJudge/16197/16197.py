# 1:46 ~ 2:22 (36분)
import sys, heapq

input = sys.stdin.readline


def bfs(hq):
    while hq:
        count, i1, j1, i2, j2 = heapq.heappop(hq)

        if count > 10:
            return -1

        for way in range(4):
            ii1 = i1 + dx[way]
            jj1 = j1 + dy[way]
            ii2 = i2 + dx[way]
            jj2 = j2 + dy[way]

            is_coin1_out = False
            is_coin2_out = False

            if ii1 < 0 or ii1 > N - 1 or jj1 < 0 or jj1 > M - 1:
                is_coin1_out = True

            if ii2 < 0 or ii2 > N - 1 or jj2 < 0 or jj2 > M - 1:
                is_coin2_out = True

            if is_coin1_out == True and is_coin2_out == True:
                continue
            elif is_coin1_out == False and is_coin2_out == False:
                if (
                    not coin1_visit[ii1][jj1][ii2][jj2]
                    and not coin2_visit[ii2][jj2][ii1][jj1]
                ):
                    coin1_visit[ii1][jj1][ii2][jj2] = True
                    coin2_visit[ii2][jj2][ii1][jj1] = True

                    if board[ii1][jj1] == "#" and board[ii2][jj2] == "#":
                        heapq.heappush(hq, (count + 1, i1, j1, i2, j2))
                    elif board[ii1][jj1] == "#":
                        heapq.heappush(hq, (count + 1, i1, j1, ii2, jj2))
                    elif board[ii2][jj2] == "#":
                        heapq.heappush(hq, (count + 1, ii1, jj1, i2, j2))
                    else:
                        heapq.heappush(hq, (count + 1, ii1, jj1, ii2, jj2))

            else:
                return count
    return -1


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

coin1_visit = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]
coin2_visit = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

hq = []

coin1 = None
coin2 = None

for i in range(N):
    for j in range(M):
        if board[i][j] == "o":
            if not coin1:
                coin1 = (i, j)
            else:
                coin2 = (i, j)

coin1_visit[coin1[0]][coin1[1]][coin2[0]][coin2[1]] = True
coin2_visit[coin2[0]][coin2[1]][coin1[0]][coin1[1]] = True


heapq.heappush(hq, (1, *coin1, *coin2))

print(bfs(hq))