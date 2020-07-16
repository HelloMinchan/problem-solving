# PyPy3 정답, Python 3 시간 초과
import sys
input = sys.stdin.readline


def check(k, x, y):
    if k in sudoku[x]:
        return False

    # zip() 쓰면 시간 초과
    # if k in list(zip(*sudoku))[y]:
    #     return False
    for i in range(9):
        if sudoku[i][y] == k:
            return False
    
    ii, jj = (x // 3) * 3, (y // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku[ii + i][jj + j] == k:
                return False

    return True
    

def DFS(depth):
    if depth == len(zeroList):    
        for line in sudoku:
            print(*line)
        sys.exit(0)
    
    for k in range(1, 10):
        x = zeroList[depth][0]
        y = zeroList[depth][1]
        
        if check(k, x, y):
            sudoku[x][y] = k
            DFS(depth + 1)
            sudoku[x][y] = 0


sudoku = [list(map(int, input().split())) for _ in range(9)]
zeroList = [(i, j) for j in range(9) for i in range(9) if sudoku[i][j] == 0]

DFS(0)
