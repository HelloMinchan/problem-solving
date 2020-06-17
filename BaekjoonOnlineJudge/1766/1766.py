import sys, heapq
input = sys.stdin.readline


def topologicalSort():
    for _ in range(N):
        if not hq:
            return
        
        target = heapq.heappop(hq)
        sequence.append(target)

        for x in adjList[target]:
            indegree[x] -= 1

            if not indegree[x]:
                heapq.heappush(hq, x)


N, M = map(int, input().split())

sequence = []
indegree = [0] * (N + 1)
adjList = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())

    indegree[B] += 1
    adjList[A].append(B)

hq = []
for i in range(1, N + 1):
    if not indegree[i]:
        heapq.heappush(hq, i)

topologicalSort()

print(*sequence)
