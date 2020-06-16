from collections import deque
import sys
input = sys.stdin.readline


def topologicalSort():
    for _ in range(N):
        if not dq:
            return
        
        target = dq.popleft()
        ans.append(target)

        for v in adjList[target]:
            indegree[v] -= 1

            if not indegree[v]:
                dq.append(v)
                

N, M = map(int, input().split())

ans = []
indegree = [0] * (N + 1)
adjList = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())

    adjList[A].append(B)
    indegree[B] += 1

dq = deque()
for i in range(1, N + 1):
    if not indegree[i]:
        dq.append(i)

topologicalSort()

print(*ans)
