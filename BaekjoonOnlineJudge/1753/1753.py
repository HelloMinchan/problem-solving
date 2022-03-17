import sys, heapq

input = sys.stdin.readline


def dijkstra(hq):
    while hq:
        weight, vertex = heapq.heappop(hq)

        if weight < dist[vertex]:
            dist[vertex] = weight

            for v, w in adj_list[vertex]:
                heapq.heappush(hq, (weight+w, v))


V, E = map(int, input().split())
K = int(input())

adj_list = [[] for _ in range(V+1)]

INF = 2147483647
dist = [INF for _ in range(V+1)]
dist[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())

    adj_list[u].append((v,w))

hq = []

for v, w in adj_list[K]:
    heapq.heappush(hq, (w, v))

dijkstra(hq)

for answer in dist[1:]:
    print(answer if answer != INF else "INF")