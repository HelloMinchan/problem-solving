import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def dfs(root):
    child_count[root] = 1

    for child_node in tree[root]:
        if not visit[child_node]:
            visit[child_node] = True

            child_count[root] += dfs(child_node)

    return child_count[root]
    


N, R, Q = map(int, input().split())

tree = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
child_count = [0 for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())

    tree[U].append(V)
    tree[V].append(U)

visit[R] = True
dfs(R)

for _ in range(Q):
    U = int(input())

    print(child_count[U])