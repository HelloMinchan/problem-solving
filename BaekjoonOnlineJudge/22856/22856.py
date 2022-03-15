from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def dfs(root):
    global last_node, edge_count

    l_node, r_node = tree[root]
    
    if l_node != -1:
        edge_count += 2
        dfs(l_node)
        
    last_node = root

    if r_node != -1:
        edge_count += 2
        dfs(r_node)

N = int(input())

tree = defaultdict(list)
last_node = 0
edge_count = 0
p_nodes = [0 for _ in range(N+1)]

for _ in range(N):
    p_node, l_node, r_node = map(int, input().split())

    tree[p_node].append(l_node)
    tree[p_node].append(r_node)

    if l_node != -1:
        p_nodes[l_node] = p_node
    
    if r_node != -1:
        p_nodes[r_node] = p_node

dfs(1)

cur_node = last_node

while cur_node != 1:
    cur_node = p_nodes[cur_node]
    edge_count -= 1

print(edge_count)