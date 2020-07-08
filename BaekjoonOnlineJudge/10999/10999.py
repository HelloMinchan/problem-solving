import sys
input = sys.stdin.readline
from math import ceil, log


def init(arr, tree, node, start, end):
    if start == end:
        tree[node][0] = arr[start]
        return tree[node][0]
    else:
        tree[node][0] = init(arr, tree, node * 2, start, (start + end) // 2) + init(arr, tree, node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node][0]


def lazyProp(tree, node, start, end, left, right, lazy):
    if tree[node][1] != 0:
        tree[node][0] += ((end - start + 1) * tree[node][1])
        if start != end:
            tree[node * 2][1] += tree[node][1]
            tree[node * 2 + 1][1] += tree[node][1]

        tree[node][1] = 0

    if (right < start or end < left):
        return
    elif (left <= start and end <= right):
        tree[node][0] += ((end - start + 1) * lazy)

        if start != end:
            tree[node * 2][1] += lazy
            tree[node * 2 + 1][1] += lazy

    else:
        lazyProp(tree, node * 2, start, (start + end) // 2, left, right, lazy)
        lazyProp(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right, lazy)

        tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]

    
def getSum(tree, node, start, end, left, right):
    if tree[node][1] != 0:
        tree[node][0] += (end - start + 1) * tree[node][1]
        if start != end:
            tree[node * 2][1] += tree[node][1]
            tree[node * 2 + 1][1] += tree[node][1]
        tree[node][1] = 0

    if right < start or end < left:
        return 0
    if left <= start and end <= right:

        if tree[node][1] != 0:
            tree[node][0] += (end - start + 1) * tree[node][1]

            if start != end:
                tree[node * 2][1] += tree[node][1]
                tree[node * 2 + 1][1] += tree[node][1]
        
            tree[node][1] = 0
        return tree[node][0]

    return getSum(tree, node * 2, start, (start + end) // 2, left, right) + getSum(tree, node * 2 + 1, (start + end) // 2 + 1, end, left, right)


N, M, K = map(int, input().split())

arr = [0] * (N + 1)

for i in range(1, N + 1):
    arr[i] = int(input())

h = ceil(log(N, 2))
tree_size = (1 << (h + 1))

tree = [[0, 0] for _ in range(tree_size)]

init(arr, tree, 1, 1, N)

for _ in range(M + K):
    order = list(map(int, input().split()))

    if order[0] == 1:
        lazyProp(tree, 1, 1, N, order[1], order[2], order[3])
    else:
        print(getSum(tree, 1, 1, N, order[1], order[2]))

