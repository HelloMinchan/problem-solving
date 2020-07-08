import sys
input = sys.stdin.readline
from math import ceil, log


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(arr, tree, node * 2, start, (start + end) // 2) + init(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]


def modify(tree, node, start, end, target, change):
    if target < start or target > end:
        return tree[node]
    if start == end:
        tree[node] = change
        return tree[node]
    tree[node] = modify(tree, node * 2, start, (start + end) // 2, target, change) + modify(tree, node * 2 + 1, (start + end) // 2 + 1, end, target, change)
    return tree[node]


def getSum(tree, node, start, end, b, c):
    if b > end or c < start:
        return 0
    if b <= start and end <= c:
        return tree[node]

    return getSum(tree, node * 2, start, (start + end) // 2, b, c) + getSum(tree, node * 2 + 1, (start + end) // 2 + 1, end, b, c)


N, M, K = map(int, input().split())

arr = [0] * N
h = ceil(log(N, 2))
tree_size = (1 << (h + 1))
tree = [0] * tree_size

for i in range(N):
    arr[i] = int(input())

init(arr, tree, 1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    if a == 1:
        modify(tree, 1, 0, N - 1, b - 1, c)
    else:
        print(getSum(tree, 1, 0, N - 1, b - 1, c - 1))
