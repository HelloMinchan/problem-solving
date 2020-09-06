import heapq


def dijkstra(hq):
    global dist, adjList
    
    while hq:
        wei, vec = heapq.heappop(hq)
        
        if dist[vec] > wei:
            dist[vec] = wei
            
            for v, w in adjList[vec]:
                heapq.heappush(hq, (w + wei, v))


def solution(N, roads, K):
    global dist, adjList
    
    answer = 0
    INF = 2147483647
    dist = [INF] * (N + 1)
    dist[1] = 0
    
    adjList = [[] for _ in range(N + 1)]
    
    for road in roads:
        sv, dv, w = road
        
        adjList[sv].append((dv, w))
        adjList[dv].append((sv, w))
    
    hq = []
    
    for dv, w in adjList[1]:
        heapq.heappush(hq, (w, dv))
    
    dijkstra(hq)
    
    for d in dist[1:]:
        if d <= K:
            answer += 1
            
    return answer
