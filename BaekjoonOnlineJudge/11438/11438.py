import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline
LENGTH = 21

def dfs(level, root):
    tree_level[root] = level

    for child_node in tree[root]:
        if p_nodes[child_node][0] == -1:
            p_nodes[child_node][0] = root

            dfs(level+1, child_node)


def set_p_nodes():
    for i in range(1, LENGTH):
        for j in range(1, N+1):
            p_nodes[j][i] = p_nodes[p_nodes[j][i - 1]][i - 1]


def lca(a, b):
    if tree_level[a] > tree_level[b]:
        a, b = b, a
    
    for i in range(LENGTH - 1, -1, -1):
        if tree_level[b] - tree_level[a] >= (1 << i):
            b = p_nodes[b][i]
    
    if a == b:
        return a
    
    for i in range(LENGTH - 1, -1, -1):
        if p_nodes[a][i] != p_nodes[b][i]:
            a = p_nodes[a][i]
            b = p_nodes[b][i]
    
    return p_nodes[a][0]


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    sv, dv = map(int, input().split())

    tree[sv].append(dv)
    tree[dv].append(sv)

p_nodes = [[-1 for _ in range(LENGTH)] for _ in range(N+1)]
tree_level = [0 for _ in range(N+1)]

p_nodes[1][0] = 0
dfs(0, 1)

set_p_nodes()

M = int(input())

for i in range(M):
    a, b = map(int, input().split())

    print(lca(a, b))