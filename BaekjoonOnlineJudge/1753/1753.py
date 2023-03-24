import sys, heapq

input = sys.stdin.readline


def dijkstra():
    while hq:
        w, v = heapq.heappop(hq)

        if dists[v] > w:
            dists[v] = w

            for next_v, next_w in adj_list[v]:
                if dists[next_v] > dists[v] + next_w:
                    heapq.heappush(hq, (dists[v] + next_w, next_v))


V, E = map(int, input().split())

K = int(input())

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())

    adj_list[u].append((v, w))

INF = sys.maxsize
dists = [INF for _ in range(V + 1)]
dists[K] = 0

hq = []
for v, w in adj_list[K]:
    heapq.heappush(hq, (w, v))

dijkstra()

for dist in dists[1:]:
    print(dist if dist != INF else "INF")
