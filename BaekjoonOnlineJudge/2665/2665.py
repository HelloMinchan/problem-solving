import sys, heapq
input = sys.stdin.readline


def BFS():
    hq = []
    visit[0][0] = True
    heapq.heappush(hq, (0, 0, 0))

    while hq:
        w, i, j = heapq.heappop(hq)

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > n - 1 or jj < 0 or jj > n - 1:
                continue
            
            if ii == n - 1 and jj == n - 1:
                return w

            if not visit[ii][jj]:
                visit[ii][jj] = True
                if not board[ii][jj]:
                    heapq.heappush(hq, (w + 1, ii, jj))
                else:
                    heapq.heappush(hq, (w, ii, jj))
        

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

print(BFS())
