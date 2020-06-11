import sys, heapq
input = sys.stdin.readline

def BFS(hq):
    while hq:
        wei, vec = heapq.heappop(hq)

        if lupy[vec] > wei:
            lupy[vec] = wei

            for w, v in adjList[vec]:
                heapq.heappush(hq, (w+wei, v))

case = 0
while 1:
    N = int(input())

    if not N:
        sys.exit(0)
    case += 1

    cave = [list(map(int,input().split())) for _ in range(N)]

    INF = 2147483647
    lupy = [INF] * (N * N)
    lupy[0] = 0
    adjList= [[] for _ in range(N*N)]

    index = 0
    for i in range(N):
        for j in range(N):
            if i-1 >= 0:
                adjList[index].append((cave[i][j], (index-N)))
            if i+1 < N:
                adjList[index].append((cave[i][j], (index+N)))
            if j-1 >= 0:
                adjList[index].append((cave[i][j], (index-1)))
            if j+1 < N:
                adjList[index].append((cave[i][j], (index+1)))

            index += 1

    hq = []
    for w, v in adjList[0]:
        heapq.heappush(hq,(w,v))

    BFS(hq)

    print("Problem %d: %d" %(case, lupy[-1]+cave[-1][-1]))