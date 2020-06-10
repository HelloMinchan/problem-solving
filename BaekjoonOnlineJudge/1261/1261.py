import sys, heapq
input = sys.stdin.readline

def BFS(hq):
    while(hq):
        wei, vec = heapq.heappop(hq)

        if di[vec] > wei:
            di[vec] = wei

            for w, v in adjList[vec]:
                heapq.heappush(hq,(w+wei, v))

N, M = map(int,input().split())
N, M = M, N
maze = [list(map(int,input().rstrip())) for _ in range(N)]

adjList = [[] for _ in range(N*M)]
INF = 2147483647
di = [INF] * (N*M)
di[0] = 0
hq = []

index = 0
for i in range(N):
    for j in range(M):
        if i-1 > -1:
            adjList[index].append((maze[i-1][j], index-M))
        if i+1 < N:
            adjList[index].append((maze[i+1][j], index+M))
        if j-1 > -1:
            adjList[index].append((maze[i][j-1], index-1))
        if j+1 < M:
            adjList[index].append((maze[i][j+1], index+1))
        index += 1

for w, v in adjList[0]:
    heapq.heappush(hq, (w, v))

BFS(hq)

print(di[-1])