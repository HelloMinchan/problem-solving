import heapq

def BFS(hq, di, adjList):
    while(hq):
        wei, vec = heapq.heappop(hq)
        
        if di[vec] > wei:
            di[vec] = wei
            
            for w, v in adjList[vec]:
                heapq.heappush(hq, (w+wei,v))
        
def solution(n, edge):
    adjList = [[] for _ in range(n+1)]
    INF = 2147483647
    di = [INF] * (n + 1)
    di[1] = 0
    hq = []
    
    for e in edge:
        adjList[e[0]].append((1,e[1]))
        adjList[e[1]].append((1,e[0]))
    
    for w, v in adjList[1]:
        heapq.heappush(hq,(w,v))
    
    BFS(hq, di, adjList)
    
    maxDistance = 0
    for d in di:
        if d != INF and maxDistance < d:
            maxDistance = d
    
    return di.count(maxDistance)