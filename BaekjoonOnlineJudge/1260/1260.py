from collections import deque
import sys

input = sys.stdin.readline

def dfs(start_node):
    for node in adj_list[start_node]:
        if not visit[node]:
            visit[node] = True
            stack.append(node)
            dfs(node)

def bfs(dq):
    while dq:
        start_node = dq.popleft()
        print(start_node, end = " ")

        for node in adj_list[start_node]:
            if not visit[node]:
                visit[node] = True
                stack.append(node)
                dq.append(node)
            

N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    sv, dv = map(int, input().split())

    adj_list[sv].append(dv)
    adj_list[dv].append(sv)

for i in range(1, N+1):
    adj_list[i].sort()


visit = [False for _ in range(N+1)]
visit[V] = True
stack = [V]
dfs(V)

print(*stack)

visit = [False for _ in range(N+1)]
visit[V] = True
dq = deque()
dq.append(V)
bfs(dq)