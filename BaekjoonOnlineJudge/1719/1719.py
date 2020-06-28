import sys, heapq
input = sys.stdin.readline


def dijkstra(sv):
    hq = []
    time = [INF] * (n + 1)
    time[sv] = 0

    for w, dv in adjList[sv]:
        routeTable[sv][dv] = dv
        heapq.heappush(hq, (w, dv , dv))

    while hq:
        wei, vec, before = heapq.heappop(hq)

        if time[vec] > wei:
            time[vec] = wei

            routeTable[sv][vec] = routeTable[sv][before]

            for w, v in adjList[vec]:
                heapq.heappush(hq, (w + wei, v, vec))


n, m = map(int, input().split())

INF = 2147483647
routeTable = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    routeTable[i][i] = '-'

adjList = [[] for _ in range(n + 1)]
for _ in range(m):
    sv, dv , w = map(int, input().split())

    adjList[sv].append((w, dv))
    adjList[dv].append((w, sv))

for i in range(1, n + 1):
    dijkstra(i)

for i in range(1, n + 1):
    print(*routeTable[i][1:])
