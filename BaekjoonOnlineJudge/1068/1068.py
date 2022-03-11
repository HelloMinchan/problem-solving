from collections import defaultdict
import sys

input = sys.stdin.readline

def dfs(start_node):
    global answer

    if delete_node in tree[start_node]:
        tree[start_node].remove(delete_node)

    if tree[start_node]:
        for node in tree[start_node]:        
            dfs(node)
    else:
        answer += 1
    


N = int(input())
p_nodes = list(map(int, input().split()))
delete_node = int(input())

answer = 0
tree = defaultdict(list)

for node, p_node in enumerate(p_nodes):
    if p_node != -1:
        tree[p_node].append(node)

for node, root in enumerate(p_nodes):
    if root == -1 and node != delete_node:
        dfs(node)
    elif root == -1 and node == delete_node:
        print(0)
        break
else:
    print(answer)