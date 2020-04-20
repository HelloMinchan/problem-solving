import sys
input = sys.stdin.readline

N = int(input())
gameBoard = [list(map(int , input().split())) for _ in range(N)]
memoization = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        ii = i
        jj = j
        
        for x in range(ii):
            if gameBoard[x][j] == i - x:
                if not x and not j:
                    memoization[i][j] = 1
                    break
                if memoization[x][j]:
                    memoization[i][j] += memoization[x][j]

        for y in range(jj):
            if gameBoard[i][y] == j - y:
                if not y and not i:
                    memoization[i][j] = 1
                    break
                if memoization[i][y]:
                    memoization[i][j] += memoization[i][y]

print(memoization[-1][-1])