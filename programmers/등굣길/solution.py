import sys
sys.setrecursionlimit(10 ** 7)


def DFS(m, n, i, j):
    global dx, dy, memoization
    
    if i == n - 1 and j == m - 1:
        return 1
    
    if memoization[i][j] >= 0:
        return memoization[i][j]
    
    memoization[i][j] = 0
    
    for way in range(2):
        ii = i + dx[way]
        jj = j + dy[way]
        
        if ii < 0 or ii > n - 1 or jj < 0 or jj > m - 1:
            continue
            
        if memoization[ii][jj] != -2:
            memoization[i][j] += DFS(m, n, ii, jj)
        
    return memoization[i][j] % 1000000007


def solution(m, n, puddles):
    global dx, dy, memoization
    
    answer = 0
    
    memoization = [[-1] * m for _ in range(n)]
    dx, dy = [1, 0], [0, 1]
    
    for p in puddles:
        memoization[p[1] - 1][p[0] - 1] = -2
    
    return DFS(m, n, 0, 0) % 1000000007
