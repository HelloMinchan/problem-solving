from collections import deque


def DFS(start_vertex):
    if len(stack) == N:
        return

    for vertex in adjacency_list[start_vertex]:
        if not visit[vertex]:
            visit[vertex] = True

            stack.append(vertex)
            DFS(vertex)


def BFS(dq):
    while dq:
        start_vertex = dq.popleft()
        answer.append(start_vertex)

        for vertex in adjacency_list[start_vertex]:
            if not visit[vertex]:
                visit[vertex] = True

                dq.append(vertex)


N, M, V = map(int, input().split())

adjacency_list = [[] for _ in range(N + 1)]

for _ in range(M):
    sv, dv = map(int, input().split())

    adjacency_list[sv].append(dv)
    adjacency_list[dv].append(sv)

for i in range(N + 1):
    adjacency_list[i].sort()

visit = [False for _ in range(N + 1)]
visit[V] = True
stack = [V]
DFS(V)
print(*stack)

visit = [False for _ in range(N + 1)]
visit[V] = True
dq = deque()
dq.append(V)
answer = []
BFS(dq)
print(*answer)