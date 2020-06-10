import sys, heapq
input = sys.stdin.readline

def BFS(hq, dt, adjList):
    while(hq):
        wei, vec = heapq.heappop(hq)

        if dt[vec] > wei:
            dt[vec] = wei

            for v, w in adjList[vec]:
                heapq.heappush(hq, (w+wei, v))


N, M, X = map(int, input().split())
adjList = [[] for _ in range(N+1)]
reverseAdjList = [[] for _ in range(N+1)]

INF = 2147483647
bdt = [INF] * (N+1)
bdt[X] = 0
sdt = [INF] * (N+1)
sdt[X] = 0
hq = []

for _ in range(M):
    a, b, w = map(int, input().split())

    adjList[a].append((b, w))
    reverseAdjList[b].append((a,w))

for v, w in adjList[X]:
    heapq.heappush(hq, (w, v))

BFS(hq, bdt, adjList)

hq = []
for v, w in reverseAdjList[X]:
    heapq.heappush(hq, (w, v))

BFS(hq, sdt, reverseAdjList)

maxTime = 0

for i in range(1, N+1):
    if i == X:
        continue

    if maxTime < sdt[i] + bdt[i]:
        maxTime = sdt[i] + bdt[i]

print(maxTime)