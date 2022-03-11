from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def dfs(level, buildings):
    root = len(buildings) // 2

    tree[level].append(buildings[root])

    if root > 0:
        dfs(level+1, buildings[:root])
        dfs(level+1, buildings[root+1:])


K = int(input())
buildings = list(map(int, input().split()))

tree = defaultdict(list)

dfs(1, buildings)

for level in tree.values():
    print(*level)