from collections import deque
import sys
input = sys.stdin.readline


def DFS(sv):
    print(sv, end=" ")

    if visit.count(True) == N:
        return

    for dv in adjList[sv]:
        if not visit[dv]:
            visit[dv] = True
            
            DFS(dv)


def BFS(V):
    dq = deque()
    dq.append(V)

    while dq:
        sv = dq.popleft()
        print(sv, end=" ")

        for dv in adjList[sv]:
            if not visit[dv]:
                visit[dv] = True
                dq.append(dv)


N, M, V = map(int, input().split())
adjList = [[] for _ in range(N + 1)]
stack = []
visit = [False] * (N + 1)

for _ in range(M):
    sv, dv = map(int, input().split())

    adjList[sv].append(dv)
    adjList[dv].append(sv)
    adjList[sv].sort()
    adjList[dv].sort()

visit[V] = True
DFS(V)

print()

visit = [False] * (N + 1)
visit[V] = True
BFS(V)
