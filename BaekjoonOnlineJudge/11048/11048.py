import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(i, j):
    if i == N and j == M:
        return maze[i][j]

    if memoization[i][j] != -1:
        return memoization[i][j]

    memoization[i][j] = maze[i][j]

    for way in range(3):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii > N - 1 or jj > M - 1:
            continue

        memoization[i][j] = max(memoization[i][j], DFS(ii, jj) + maze[i][j])
    
    return memoization[i][j]


N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]

memoization = [[-1] * M for _ in range(N)]
dx, dy = [0, 1, 1], [1, 0, 1]

print(DFS(0, 0))
