from collections import deque
import sys

input = sys.stdin.readline


def dfs(start):
    for node in adj_list[start]:
        if not visit[node]:
            visit[node] = True
            dfs_answer.append(node)
            dfs(node)


def bfs(dq):
    while dq:
        start = dq.popleft()
        bfs_answer.append(start)

        for node in adj_list[start]:
            if not visit[node]:
                visit[node] = True
                dq.append(node)


N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    sv, dv = map(int, input().split())

    adj_list[sv].append(dv)
    adj_list[dv].append(sv)

for i in range(1, N+1):
    adj_list[i].sort()

dfs_answer = [V]
visit = [False for _ in range(N+1)]
visit[V] = True
dfs(V)

print(*dfs_answer)

dq = deque()
dq.append(V)
visit = [False for _ in range(N+1)]
visit[V] = True

bfs_answer = []
bfs(dq)

print(*bfs_answer)