import sys
input = sys.stdin.readline


def DFS(N):
    if N == 1 or N == 0:
        return stairs[N]
    
    if N == 2:
        return stairs[1] + stairs[2]

    if memoization[N] != -1:
        return memoization[N]

    memoization[N] = max(DFS(N - 3) + stairs[N - 1] + stairs[N], DFS(N - 2) + stairs[N])

    return memoization[N]


N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
memoization = [-1] * (N + 1)

print(DFS(N))

