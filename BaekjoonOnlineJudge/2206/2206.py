import sys, heapq
input = sys.stdin.readline


def BFS(x, y):
    hq = []
    visit[0][x][y] = True
    visit[1][x][y] = True
    heapq.heappush(hq, (1, 0, x, y))

    while hq:
        d, w, i, j = heapq.heappop(hq)
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if ii == N - 1 and jj == M - 1:
                if w < 2:
                    return d + 1

            if not visit[w][ii][jj]:
                visit[w][ii][jj] = True
                if board[ii][jj] == 1:
                    if w + 1 > 1:
                        visit[w][ii][jj] = False
                        continue
                    heapq.heappush(hq , (d + 1, w + 1, ii, jj))
                else:
                    heapq.heappush(hq, (d + 1, w, ii, jj))
                    
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]

if N + M == 2:
    print(1)
    sys.exit(0)

visit = [[[False] * M for _ in range(N)] for _ in range(2)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

print(BFS(0, 0))
