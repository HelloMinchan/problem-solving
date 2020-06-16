from collections import deque
import sys
input = sys.stdin.readline


def topologicalSort():
    for _ in range(N):
        if not dq:
            return

        target = dq.popleft()

        for x in adjList[target]:
            sequence[x] = max(sequence[x], sequence[target] + D[x])
            indegree[x] -= 1
            
            if not indegree[x]:
                dq.append(x)


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    sequence = [0] * (N + 1)
    indegree = [0] * (N + 1)
    adjList = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())

        indegree[Y] += 1
        adjList[X].append(Y)
    
    W = int(input())

    dq = deque()
    for i in range(1, N + 1):
        if not indegree[i]:
            sequence[i] = D[i]
            dq.append(i)

    topologicalSort()

    print(sequence[W])
