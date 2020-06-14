import sys, heapq
input = sys.stdin.readline


def dij(hq):
    while(hq):
        wei, vec = heapq.heappop(hq)

        if dist[vec] > wei:
            dist[vec] = wei
            
            for w, v in adjList[vec]:
                heapq.heappush(hq, (w + wei, v))


N, M = map(int, input().split())

INF = 2147483647
dist = [INF for _ in range(N + 1)]
dist[1] = 0

adjList = [[] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    adjList[a].append((1, b))
    adjList[b].append((1, a))

hq = []
for w, v in adjList[1]:
    heapq.heappush(hq, (w, v))

dij(hq)

print(dist.index(max(dist[1:])), max(dist[1:]), dist.count(max(dist[1:])))
