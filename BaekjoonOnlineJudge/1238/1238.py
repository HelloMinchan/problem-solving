import sys, heapq

input = sys.stdin.readline


def dijkstra(adj_list):
    INF = sys.maxsize
    dists = [INF for _ in range(N + 1)]
    dists[X] = 0

    hq = []
    for v, w in adj_list[X]:
        heapq.heappush(hq, (w, v))

    while hq:
        w, v = heapq.heappop(hq)

        if dists[v] > w:
            dists[v] = w

            for next_v, next_w in adj_list[v]:
                if dists[next_v] > dists[v] + next_w:
                    heapq.heappush(hq, (dists[v] + next_w, next_v))

    for index, dist in enumerate(dists):
        answer[index] += dist


N, M, X = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
reversed_adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    sv, dv, w = map(int, input().split())

    adj_list[sv].append((dv, w))
    reversed_adj_list[dv].append((sv, w))

answer = [0 for _ in range(N + 1)]

dijkstra(adj_list)
dijkstra(reversed_adj_list)

print(max(answer[1:]))
