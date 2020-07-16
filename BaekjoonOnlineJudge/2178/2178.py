import sys, heapq
input = sys.stdin.readline


def BFS(i, j):
    hq = []
    visit[i][j] = True
    heapq.heappush(hq, (1, i, j))

    while hq:
        count, i, j = heapq.heappop(hq)

        if i == N - 1 and j == M - 1:
            return count
        
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if not visit[ii][jj] and maze[ii][jj] == '1':
                visit[ii][jj] = True
                heapq.heappush(hq, (count + 1, ii, jj))


N, M = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(N)]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
visit = [[False] * M for _ in range(N)]

print(BFS(0, 0))
