import sys, heapq

input = sys.stdin.readline

INF = sys.maxsize


def dijkstra():
    while hq:
        w, v = heapq.heappop(hq)

        if hacking_times[v] > w:
            hacking_times[v] = w

            for next_v, next_w in adj_list[v]:
                if hacking_times[next_v] > hacking_times[v] + next_w:
                    heapq.heappush(hq, (hacking_times[v] + next_w, next_v))


test_case = int(input())
for _ in range(test_case):
    n, d, c = map(int, input().split())

    adj_list = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())

        adj_list[b].append((a, s))

    hacking_times = [INF for _ in range(n + 1)]
    hacking_times[c] = 0

    hq = []
    for v, w in adj_list[c]:
        heapq.heappush(hq, (w, v))

    dijkstra()

    hacking_count = 0
    max_hacking_time = 0
    for hacking_time in hacking_times[1:]:
        if hacking_time != INF:
            hacking_count += 1
            max_hacking_time = max(max_hacking_time, hacking_time)

    print(hacking_count, max_hacking_time)
