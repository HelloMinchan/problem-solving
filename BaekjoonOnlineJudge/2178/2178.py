# 5:42 ~ 5:52 (10분)
import heapq
import sys

input = sys.stdin.readline


def dijkstra(hq):
    global answer
    while hq:
        wei, i, j = heapq.heappop(hq)

        if i == N - 1 and j == M - 1:
            return wei

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if maze[ii][jj] == "1" and not visit[ii][jj]:
                visit[ii][jj] = True
                heapq.heappush(hq, (wei + 1, ii, jj))


answer = 0
N, M = map(int, input().split())

maze = [list(input().rstrip()) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

hq = []
visit[0][0] = True
heapq.heappush(hq, (1, 0, 0))

print(dijkstra(hq))