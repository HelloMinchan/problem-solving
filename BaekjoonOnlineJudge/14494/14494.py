import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(i, j):
    # 기저 사례
    if i == n + 1 or j == m + 1:
        return 0
    if i == n and j == m:
        return 1
    if memoization[i][j] != -1:
        return memoization[i][j]

    memoization[i][j] = sum([DFS(i, j + 1), DFS(i + 1, j), DFS(i + 1, j + 1)]) % (
        1e9 + 7
    )

    return memoization[i][j]


n, m = map(int, input().split())
memoization = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

print(int(DFS(1, 1) % (1e9 + 7)))