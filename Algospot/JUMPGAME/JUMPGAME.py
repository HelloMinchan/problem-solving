import sys
input = sys.stdin.readline


def DFS(i, j):
    if i > n - 1 or j > n - 1:
        return 0
    if i == n - 1 and j == n - 1:
        return 1
    
    if memoization[i][j] != -1:
        return 0
    
    memoization[i][j] = 0

    return DFS(i + ground[i][j], j) or DFS(i, j + ground[i][j])


C = int(input())

for _ in range(C):
    n = int(input())
    ground = [list(map(int, input().split())) for _ in range(n)]
    memoization = [[-1] * n for _ in range(n)]

    print("YES" if DFS(0, 0) else "NO")