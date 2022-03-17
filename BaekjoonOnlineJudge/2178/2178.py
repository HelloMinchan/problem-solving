import sys, heapq

input = sys.stdin.readline


def bfs(hq):
    while hq:
        count, i, j = heapq.heappop(hq)

        if i == N - 1 and j == M - 1:
            print(count)
            return

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if not visit[ii][jj] and maze[ii][jj] == "1":
                visit[ii][jj] = True
                heapq.heappush(hq, (count+1, ii, jj))


N, M = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

visit[0][0] = True
hq = [(1, 0, 0)]

bfs(hq)