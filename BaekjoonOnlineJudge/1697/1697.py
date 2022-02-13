# 7:06 ~ 7:31 (25분)
import sys, heapq

input = sys.stdin.readline


def BFS(hq):
    while hq:
        before_sec, before_loc = heapq.heappop(hq)

        if before_loc == K:
            return before_sec

        for way in range(2):
            new_loc = before_loc + dx[way]

            if new_loc < 0 or new_loc > 100000:
                continue

            if dist[new_loc] > before_sec + 1:
                dist[new_loc] = before_sec + 1

                heapq.heappush(hq, (before_sec + 1, new_loc))

        new_loc = before_loc * 2
        if new_loc < 0 or new_loc > 100000:
            continue

        if dist[new_loc] > before_sec + 1:
            dist[new_loc] = before_sec + 1

            heapq.heappush(hq, (before_sec + 1, new_loc))

    print(hq)


N, K = map(int, input().split())
INF = 2147483647
dist = [INF for _ in range(100001)]
dist[N] = 0

dx = [-1, 1]
hq = []

heapq.heappush(hq, (0, N))

print(BFS(hq))