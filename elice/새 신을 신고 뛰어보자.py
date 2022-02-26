import sys

input = sys.stdin.readline

def dfs(i, j):
    if i == N - 1 and j == N - 1:
        return 1
    if i > N - 1 or j > N - 1:
        return 0
    if board[i][j] == 0:
        return 0
    
    if dp_table[i][j]:
        return dp_table[i][j]
    
    ii = i + board[i][j]
    jj = j + board[i][j]

    if ii < N:
        dp_table[i][j] += dfs(ii, j)
    if jj < N:
        dp_table[i][j] += dfs(i, jj)

    return dp_table[i][j]


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dp_table = [[0 for _ in range(N)] for _ in range(N)]

print(dfs(0,0))
