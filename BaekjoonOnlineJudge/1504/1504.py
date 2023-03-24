import sys, heapq

input = sys.stdin.readline


def dijkstra():
    while hq:
        w, v = heapq.heappop(hq)

        if dists[v] > w:
            dists[v] = w

            for next_v, next_w in adj_list[v]:
                if dists[next_v] > dists[v] + next_w:
                    heapq.heappush(hq, (dists[v] + next_w, next_v))


N, E = map(int, input().split())

INF = sys.maxsize
adj_list = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

v1, v2 = map(int, input().split())

itinerarys = [[(1, v1), (v1, v2), (v2, N)], [(1, v2), (v2, v1), (v1, N)]]

answer = []
for itinerary in itinerarys:
    total_dist = 0
    for travel in itinerary:
        departure, destination = travel

        dists = [INF for _ in range(N + 1)]
        dists[departure] = 0

        hq = []
        for v, w in adj_list[departure]:
            heapq.heappush(hq, (w, v))

        dijkstra()

        if dists[destination] != INF:
            total_dist += dists[destination]
        else:
            total_dist = INF
            break

    answer.append(total_dist)

print(min(answer) if min(answer) != INF else -1)
