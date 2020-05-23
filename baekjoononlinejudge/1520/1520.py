import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def DFS(i, j):
    if not i and not j:
        return 1;
    if (i < 0 or i >= N or j < 0 or j >= M):
        return 0;
    if memoization[i][j] != -1:
        return memoization[i][j];
    
    memoization[i][j] = 0

    for way in range(4):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii < 0 or ii >= N or jj < 0 or jj >= M:
            continue
        
        if MAP[ii][jj] > MAP[i][j]:
            memoization[i][j] += DFS(ii, jj)

    return memoization[i][j]
    

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
memoization = [[-1] * M for _ in range(N)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

print(DFS(N - 1, M - 1))