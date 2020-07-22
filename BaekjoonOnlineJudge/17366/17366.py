import sys, heapq
input = sys.stdin.readline


def dijkstra(hq):
    while hq:
        wei, vec = heapq.heappop(hq)

        if dist[vec] > wei:
            memoization[s][vec] = wei
            memoization[vec][s] = wei
            dist[vec] = wei

            for w, v in adjList[vec]:
                heapq.heappush(hq, (wei + w, v))


N, Q = map(int, (input().split()))
string = input().rstrip()
memoization = [[-1] * (N + 1) for _ in range(N + 1)]

adjList = [[] for _ in range(N + 1)]
for v in range(1, N):
    adjList[v].append((1, v + 1))
    adjList[v + 1].append((1, v))

stack = []
for i in range(N):
    if string[i] == '(':
        stack.append(i + 1)
    elif string[i] == ')':
        j = stack.pop()
        adjList[i + 1].append((2, j))
        adjList[j].append((2, i + 1))

for _ in range(Q):
    INF = 2147483647
    dist = [INF] * (N + 1)

    s, e = map(int, input().split())

    if memoization[s][e] != -1:
        print(memoization[s][e])
        continue

    hq = []
    for w, dv in adjList[s]:
        heapq.heappush(hq, (w, dv))

    dijkstra(hq)
    
    print(dist[e])
    
