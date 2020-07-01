import sys, heapq
input = sys.stdin.readline


def opp(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n == 3:
        return 4
    else:
        return 3


def BFS(x, y, di, order):
    hq = []
    visit[di][x][y] = True
    heapq.heappush(hq, (order, x, y, di))

    while hq:
        order, i, j, di = heapq.heappop(hq)

        if i == finish[0] - 1 and j == finish[1] - 1 and di == finish[2]:
            return order

        for go in range(1, 4):
            ii = i + dx[di] * go
            jj = j + dy[di] * go
            
            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if factory[ii][jj]:
                break
            
            if not visit[di][ii][jj]:
                visit[di][ii][jj] = True
                heapq.heappush(hq, (order + 1, ii, jj, di))

        for way in range(1, 5):
            if way == di:
                continue
                
            if not visit[way][i][j]:
                if di == way or di == opp(way):
                    continue
                visit[way][i][j] = True
                heapq.heappush(hq, (order + 1, i, j, way))

   
N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]
visit = [[[False] * M for _ in range(N)] for _ in range(5)]

# 공백 : 0, 동 : 1, 서 : 2, 남 : 3, 북 : 4 
dx , dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

start = list(map(int, input().split()))
finish = list(map(int, input().split()))

# 파라미터 : 행, 열, 방향, 명령 횟수
print(BFS(start[0] - 1, start[1] - 1, start[2], 0))
