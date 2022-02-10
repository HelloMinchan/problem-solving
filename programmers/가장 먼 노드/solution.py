import heapq


def dijkstra(hq):
    global dist, adjacency_list

    while hq:
        wei, vertex = heapq.heappop(hq)

        if dist[vertex] > wei:
            dist[vertex] = wei

            for v in adjacency_list[vertex]:
                heapq.heappush(hq, (wei + 1, v))


def solution(n, edge):
    global dist, adjacency_list
    answer = 0
    INF = 2147483647
    dist = [INF for _ in range(n + 1)]
    dist[1] = 0

    adjacency_list = [[] for _ in range(n + 1)]

    for sv, dv in edge:
        adjacency_list[sv].append(dv)
        adjacency_list[dv].append(sv)

    hq = []

    for v in adjacency_list[1]:
        heapq.heappush(hq, (1, v))

    dijkstra(hq)

    maximum = 0
    for d in dist:
        if d != INF and maximum < d:
            maximum = d

    answer = dist.count(maximum)

    return answer