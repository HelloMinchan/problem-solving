import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dfs(level, root):
    tree_level[root] = level

    for child_node in tree[root]:
        if p_nodes[child_node] == -1:
            p_nodes[child_node] = root

            dfs(level+1, child_node)


def lca(a, b):
    while tree_level[a] != tree_level[b]:
        if tree_level[a] > tree_level[b]:
            a = p_nodes[a]
        else:
            b = p_nodes[b]
    
    while a != b:
        a = p_nodes[a]
        b = p_nodes[b]
    
    return a


N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s_node, d_node = map(int, input().split())

    tree[s_node].append(d_node)
    tree[d_node].append(s_node)


p_nodes = [-1 for _ in range(N+1)]
tree_level = [0 for _ in range(N+1)]

p_nodes[1] = 0
dfs(0, 1)

M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    print(lca(a, b))
