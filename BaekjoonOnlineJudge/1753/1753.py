import sys, heapq
input = sys.stdin.readline

def BFS(hq):
    global distance

    while(hq):
        wei, vec = heapq.heappop(hq)

        if distance[vec] > wei:
            distance[vec] = wei

            for v, w in adjList[vec]:
                heapq.heappush(hq, (w+wei,v))

V, E = map(int,input().split())
INF = 2147483647
distance = [INF] * (V+1)
K = int(input())
distance[K] = 0
adjList = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,w = map(int,input().split())
    adjList[a].append((b,w))

hq = []

for v, w in adjList[K]:
    heapq.heappush(hq, (w,v))

BFS(hq)

for d in distance[1:]:
    if d ==INF:
        print("INF")
        continue
    print(d)