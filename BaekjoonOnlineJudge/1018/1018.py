import sys
input = sys.stdin.readline

board = []
paint = 64

N, M = map(int, input().split())

for _ in range(N):
    board.append(list(input()))

for i in range(N - 7):
    for j in range(M - 7):
        countWStart = 0
        countBStart = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                # 맨 왼쪽 위 칸이 흰색인 경우
                if l % 2 == 0:
                    if k % 2 == 0:
                        if board[k][l] != "W":
                            countWStart += 1
                    else:
                        if board[k][l] != "B":
                            countWStart += 1
                else:
                    if k % 2 == 0:
                        if board[k][l] != "B":
                            countWStart += 1
                    else:
                        if board[k][l] != "W":
                            countWStart += 1
                # 맨 왼쪽 위 칸이 검은색인 경우
                if l % 2 == 0:
                    if k % 2 == 0:
                        if board[k][l] != "B":
                            countBStart += 1
                    else:
                        if board[k][l] != "W":
                            countBStart += 1
                else:
                    if k % 2 == 0:
                        if board[k][l] != "W":
                            countBStart += 1
                    else:
                        if board[k][l] != "B":
                            countBStart += 1

        if paint > min(countWStart, countBStart):
            paint = min(countWStart, countBStart)
         
print(paint)