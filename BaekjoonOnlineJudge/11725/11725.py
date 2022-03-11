import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(start_node):
    for node in tree[start_node]:
        if not parents_node[node]:
            parents_node[node] = start_node
            dfs(node)

N = int(input())

parents_node = [0 for _ in range(N+1)]
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    p_node, c_node = map(int, input().split())

    tree[p_node].append(c_node)
    tree[c_node].append(p_node)

dfs(1)

for i in range(2, N+1):
    print(parents_node[i])