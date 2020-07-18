from math import ceil, log
import sys
input = sys.stdin.readline


def init_tree(nums, segTree, node, start, end):
    if start == end:
        segTree[node] = nums[start]
        return segTree[node] 
    else:
        segTree[node] = ((init_tree(nums, segTree, node * 2, start, (start + end) // 2) % 1000000007) * (init_tree(nums, segTree, node * 2 + 1, (start + end) // 2 + 1, end) % 1000000007)) % 1000000007
        return segTree[node]


def modify(nums, segTree, node, start, end, target, change):
    if end < target or target < start:
        return segTree[node]
    if start == end:
        segTree[node] = change
        return segTree[node]
    
    segTree[node] = ((modify(nums, segTree, node * 2, start, (start + end) // 2, target, change) % 1000000007) * (modify(nums, segTree, node * 2 + 1, (start + end) // 2 + 1, end, target, change) % 1000000007)) % 1000000007
    return segTree[node]


def getValue(nums, segTree, node, start, end, b, c):
    if end < b or c < start:
        return 1
    if b <= start and end <= c:
        return segTree[node]
    
    return ((getValue(nums, segTree, node * 2, start, (start + end) // 2, b, c) % 1000000007) * (getValue(nums, segTree, node * 2 + 1, (start + end) // 2 + 1, end, b, c) % 1000000007)) % 1000000007


N, M, K = map(int, input().split())
nums = [0] + [int(input()) for _ in range(N)]

h = ceil(log(N, 2))
treeSize = (1 << (h + 1))
segTree = [0 for _ in range(treeSize)]

init_tree(nums, segTree, 1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        modify(nums, segTree, 1, 1, N, b, c)
    else:
        print(getValue(nums, segTree, 1, 1, N, b, c))
