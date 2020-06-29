import sys
input = sys.stdin.readline


def DFS(move, x, y):
    # 기저 사례 (도착지에 도착 한 경우)
    if move == len(magicStr) - 1:
        memoization[move][x][y] = 1 
        return memoization[move][x][y]
    
    # 기저 사례 (이미 와봤던 길인 경우)
    if memoization[move][x][y] != -1:
        return memoization[move][x][y]

    memoization[move][x][y] = 0

    # 악마의 다리에서 온 경우
    if x == 0:
        for j in range(y + 1, len(bridge[0])):
            if bridge[1][j] == magicStr[move + 1]:
                memoization[move][x][y] += DFS(move + 1, 1, j)
    # 천사의 다리에서 온 경우
    else:
        for j in range(y + 1, len(bridge[0])):
            if bridge[0][j] == magicStr[move + 1]:
                memoization[move][x][y] += DFS(move + 1, 0, j)
    
    return memoization[move][x][y]
    

magicStr = input().rstrip()
bridge = [list(input().rstrip()) for _ in range(2)]
memoization = [[[-1] * len(bridge[0]) for _ in range(2)] for _ in range(len(magicStr))]

count = 0
for i in range(2):
    for j in range(len(bridge[0])):
        if bridge[i][j] == magicStr[0]:
            count += DFS(0, i, j)
            
print(count)
