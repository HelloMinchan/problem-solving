import sys
input = sys.stdin.readline
from math import log, ceil


def init(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = min(init(arr, tree, node * 2, start, (start + end) // 2), init(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end))
        return tree[node]


def findMin(tree, node, start, end, a, b):
    if b < start or end < a:
        return 2147483647
    elif a <= start and  end <= b:
        return tree[node]
    else:
        findA = findMin(tree, node * 2, start, (start + end) // 2, a, b)
        findB = findMin(tree, node * 2 + 1, (start + end) // 2 + 1, end, a, b)

        return min(findA, findB)


N, M = map(int, input().split())

arr = [0] * (N + 1)

for i in range(1, N + 1):
    arr[i] = int(input())

h = ceil(log(N, 2))
tree_size = (1 << (h + 1))

tree = [0] * tree_size

init(arr, tree, 1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())

    print(findMin(tree, 1, 1, N, a, b))
