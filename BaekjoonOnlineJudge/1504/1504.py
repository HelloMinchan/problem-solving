import sys, heapq
input = sys.stdin.readline

def BFS(hq):
    while hq:
        wei, vec = heapq.heappop(hq)
        
        if di[vec] > wei:
            di[vec] = wei

            for w, v in adjList[vec]:
                heapq.heappush(hq, (w+wei, v))

N, E = map(int,input().split())

ans = [0, 0]

INF = 2147483647
adjList = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int,input().split())

    adjList[a].append((c,b))
    adjList[b].append((c,a))

stopOver = list(map(int,input().split()))
itinerary = [[1,stopOver[0],stopOver[1],N], [1,stopOver[1],stopOver[0],N]]

for i in range(2):
    for j in range(3):
        di = [INF] * (N+1)
        di[itinerary[i][j]] = 0
        hq = []
        for w, v in adjList[itinerary[i][j]]:
            heapq.heappush(hq,(w,v))
        BFS(hq)
        ans[i] += di[itinerary[i][j+1]]

print(min(ans) if min(ans) < INF else -1)