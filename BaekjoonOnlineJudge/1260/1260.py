from collections import deque
import sys
input = sys.stdin.readline


def DFS(sv):
    print(sv, end=' ')
    for dv in adjList[sv]:
        if not visit[dv]:
            visit[dv] = True
            DFS(dv)


def BFS(sv):
    dq = deque()
    visit[sv] = True
    dq.append(sv)

    while dq:
        sv = dq.popleft()
        print(sv, end=' ')
        
        for dv in adjList[sv]:
            if not visit[dv]:
                visit[dv] = True
                dq.append(dv)


N, M, V = map(int, input().split())

adjList = [[] for _ in range(N + 1)]

for _ in range(M):
    sv, dv = map(int, input().split())

    adjList[sv].append(dv)
    adjList[sv].sort()
    adjList[dv].append(sv)
    adjList[dv].sort()

visit = [False] * (N + 1)
visit[V] = True
DFS(V)

print()

visit = [False] * (N + 1)
BFS(V)
