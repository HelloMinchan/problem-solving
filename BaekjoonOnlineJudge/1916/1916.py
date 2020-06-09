import sys, heapq
input = sys.stdin.readline

def BFS(hq):
    while(hq):
        wei, vec = heapq.heappop(hq)

        if distance[vec] > wei:
            distance[vec] = wei

            for v, w in adjList[vec]:
                heapq.heappush(hq,(w+wei, v))

N = int(input())
M = int(input())

INF = 2147483647
distance = [INF] * (N+1)
adjList = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,w = map(int,input().split())
    adjList[a].append((b,w))

S, A = map(int,input().split())

hq = []

for v, w in adjList[S]:
    heapq.heappush(hq, (w,v))

BFS(hq)

print(distance[A])