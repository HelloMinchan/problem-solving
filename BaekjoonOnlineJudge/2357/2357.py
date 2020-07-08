import sys
input = sys.stdin.readline
from math import ceil, log


def initMin(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = min(initMin(arr, tree, node * 2, start, (start + end) // 2), initMin(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end))
        
        return tree[node]


def initMax(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = max(initMax(arr, tree, node * 2, start, (start + end) // 2), initMax(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end))
        
        return tree[node]


def findMin(tree, node, start, end, a, b):
    if b < start or end < a:
        return 2147483647
    elif a <= start and end <= b:
        return tree[node]
    else:
        findA = findMin(tree, node * 2, start, (start + end) // 2, a, b)
        findB = findMin(tree, node * 2 + 1, (start + end) // 2 + 1, end, a, b)

        return min(findA, findB)


def findMax(tree, node, start, end, a, b):
    if b < start or end < a:
        return -2147483647
    elif a <= start and end <= b:
        return tree[node]
    else:
        findA = findMax(tree, node * 2, start, (start + end) // 2, a, b)
        findB = findMax(tree, node * 2 + 1, (start + end) // 2 + 1, end, a, b)

        return max(findA, findB)


N, M = map(int, input().split())

arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

h = ceil(log(N, 2))
tree_size = (1 << (h + 1))

min_tree = [0] * tree_size
max_tree = [0] * tree_size

initMin(arr, min_tree, 1, 1, N)
initMax(arr, max_tree, 1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())

    print(findMin(min_tree, 1, 1, N, a, b), end=" ")
    print(findMax(max_tree, 1, 1, N, a, b))

