import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(i, j):
    if memoization[i][j] != -1:
        return memoization[i][j]
    
    if i == N - 1 and j == M - 1:
        return 1
    
    memoization[i][j] = 0

    for way in range(4):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
            continue
        
        if MAP[i][j] > MAP[ii][jj]:
            memoization[i][j] += DFS(ii, jj)
    
    return memoization[i][j]


N, M = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(N)]
memoization = [[-1] * M for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

print(DFS(0, 0))
