import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node):
    visit[node] = True
    dp[node][1] = weights[node]
    paths[node][1].append(node)

    for child in tree[node]:
        if not visit[child]:
            result = dfs(child)

            dp[node][0] += max(dp[child][0], dp[child][1])
            dp[node][1] += dp[child][0]

            paths[node][1] += result[0]
            if dp[child][0] > dp[child][1]:
                paths[node][0] += result[0]
            else:
                paths[node][0] += result[1]

    return paths[node]


n = int(input())
weights = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())

    tree[u].append(v)
    tree[v].append(u)

visit = [False for _ in range(n + 1)]
paths = [[[] for _ in range(2)] for _ in range(n + 1)]
dp = [[0, 0] for _ in range(n + 1)]

path = dfs(1)

if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    path[0].sort()
    print(*path[0])
else:
    print(dp[1][1])
    path[1].sort()
    print(*path[1])
