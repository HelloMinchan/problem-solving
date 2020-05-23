import sys
input = sys.stdin.readline


def DFS():
    global ans
    i, j, = -1, -1
    isFinish = True

    for x in range(H):
        for y in range(W):
            if not visit[x][y]:
                isFinish = False
                i, j = x, y
                break
        if not isFinish:
            break
    
    if isFinish:
        ans += 1
        return

    if not visit[i][j]:
        for rotate in range(4):
            isPossible = True
            possibleDirection = []

            for way in range(3):
                ii = i + dx[rotate][way]
                jj = j + dy[rotate][way]

                if ii < 0 or ii > H - 1 or jj < 0 or jj > W - 1:
                    isPossible = False
                    break

                if visit[ii][jj]:
                    isPossible = False
                    break

                possibleDirection.append((ii, jj))

            if isPossible:
                for pDX, pDY in possibleDirection:
                    visit[pDX][pDY] = True

                DFS()
                
                for pDX, pDY in possibleDirection:
                    visit[pDX][pDY] = False
                        

C = int(input())
dx = [[0, 1, 1], [0, 1, 0], [0, 1, 1], [0, 0, 1]]
dy = [[0, 0, -1], [0, 0, 1], [0, 0, 1], [0, 1, 1]]

for _ in range(C):
    ans = 0
    H, W = map(int, input().split())
    gameBoard = [list(input().rstrip()) for _ in range(H)]

    visit = [[False] * W for _ in range(H)]
    whiteSection = 0
    
    for i in range(H):
        for j in range(W):
            if gameBoard[i][j] == "#":
                visit[i][j] = True
            else:
                whiteSection += 1

    if whiteSection % 3:
        print(0)
        continue

    DFS()

    print(ans)