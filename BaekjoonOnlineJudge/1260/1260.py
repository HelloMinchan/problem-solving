from collections import deque
import sys
input = sys.stdin.readline

def dfs(sv):
    visit[sv] = True    

    for dv in adj_list[sv]:
        if not visit[dv]:
            stack.append(dv)
            dfs(dv)
    
    return True

def bfs(dq):
    while dq:
        sv = dq.popleft()
        answer.append(sv)

        for dv in adj_list[sv]:
            if not visit[dv]:
                visit[dv] = True
                dq.append(dv)


N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    sv, dv = map(int, input().split())

    adj_list[sv].append(dv)
    adj_list[dv].append(sv)

for i in range(1, N+1):
    adj_list[i].sort()

visit = [False for _ in range(N+1)]
stack = [V]
dfs(V)

print(*stack)

visit = [False for _ in range(N+1)]
dq = deque()
dq.append(V)
visit[V] = True

answer = []
bfs(dq)

print(*answer)