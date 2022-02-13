# 9:11 ~

import sys, heapq

input = sys.stdin.readline


def dijkstra(hq):
    while hq:
        before_dist, i, j, break_count = heapq.heappop(hq)

        if i == N - 1 and j == M - 1:
            return before_dist

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if board[ii][jj] == "0":
                if dist[break_count][ii][jj] > before_dist + 1:
                    dist[break_count][ii][jj] = before_dist + 1
                    heapq.heappush(hq, (before_dist + 1, ii, jj, break_count))
            else:
                if break_count == 0:
                    if dist[break_count + 1][ii][jj] > before_dist + 1:
                        dist[break_count + 1][ii][jj] = before_dist + 1
                        heapq.heappush(hq, (before_dist + 1, ii, jj, break_count + 1))

    return -1


N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]
INF = 2147483647
dist = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(2)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

hq = []

dist[0][0][0] = 0
dist[1][0][0] = 0

heapq.heappush(hq, (1, 0, 0, 0))

print(dijkstra(hq))