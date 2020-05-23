import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def DFS(i, j):
    if memoization[i][j]:
        return memoization[i][j]
    
    memoization[i][j] = 1

    for way in range(4):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii < 0 or ii > n - 1 or jj < 0 or jj > n - 1:
            continue

        if bambooForest[i][j] < bambooForest[ii][jj]:
            day = DFS(ii, jj) + 1
            
            if memoization[i][j] < day:
                memoization[i][j] = day
    
    return memoization[i][j]


n = int(input())
bambooForest = [list(map(int, input().split())) for _ in range(n)]
memoization = [[0] * n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
maxAliveDay = 0

for i in range(n):
    for j in range(n):
        aliveDay = DFS(i, j)
        if maxAliveDay < aliveDay:
            maxAliveDay = aliveDay

print(maxAliveDay)