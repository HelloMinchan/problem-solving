# 9:39 ~ 9:51 (12분)

import sys, heapq

input = sys.stdin.readline


def dijkstra(hq):
    while hq:
        before_dist, i, j = heapq.heappop(hq)

        if i == end_i and j == end_j:
            return before_dist

        for way in range(8):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > length - 1 or jj < 0 or jj > length - 1:
                continue

            if dist[ii][jj] > before_dist + 1:
                dist[ii][jj] = before_dist + 1
                heapq.heappush(hq, (before_dist + 1, ii, jj))


T = int(input())

for _ in range(T):
    length = int(input())
    start_i, start_j = tuple(map(int, input().split()))
    end_i, end_j = tuple(map(int, input().split()))

    dx = [-2, -1, -2, -1, 1, 2, 1, 2]
    dy = [-1, -2, 1, 2, -2, -1, 2, 1]

    INF = 2147483647
    dist = [[INF for _ in range(length)] for _ in range(length)]

    hq = []

    dist[start_i][start_j] = 0
    heapq.heappush(hq, (0, start_i, start_j))

    print(dijkstra(hq))
