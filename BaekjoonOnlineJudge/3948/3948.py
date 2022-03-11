import sys

input = sys.stdin.readline


def dfs(N, K):
    if not K:
        if not N:
            return 1
        else:
            return 0

    if dp_table[N][K] != -1:
        return dp_table[N][K]
    
    dp_table[N][K] = dfs(N, K-1) + dfs(N-1, N-K)
    
    return dp_table[N][K]


T = int(input())

for _ in range(T):
    N = int(input())

    dp_table = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    dp_table[0][0] = 1

    if N == 1:
        print(1)
    else:
        print(dfs(N, N) * 2)