from collections import defaultdict
import sys

input = sys.stdin.readline


def pre_dfs(start_node):
    pre_answer.append(start_node)

    if tree[start_node][0] != ".":
        pre_dfs(tree[start_node][0])
    
    if tree[start_node][1] != ".":
        pre_dfs(tree[start_node][1])


def mid_dfs(start_node):
    if tree[start_node][0] != ".":
        mid_dfs(tree[start_node][0])

    mid_answer.append(start_node)

    if tree[start_node][1] != ".":
        mid_dfs(tree[start_node][1])


def post_dfs(start_node):
    if tree[start_node][0] != ".":
        post_dfs(tree[start_node][0])

    if tree[start_node][1] != ".":
        post_dfs(tree[start_node][1])
    
    post_answer.append(start_node)
    

N = int(input())

tree = defaultdict(list)

for _ in range(N):
    node, left_node, right_node = input().split()

    tree[node].append(left_node)
    tree[node].append(right_node)

pre_answer = []
pre_dfs("A")
print("".join(pre_answer))

mid_answer = []
mid_dfs("A")
print("".join(mid_answer))

post_answer = []
post_dfs("A")
print("".join(post_answer))