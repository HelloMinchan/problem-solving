import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
answer = 987654321

for i in range(0, N - 7):
    for j in range(0, M - 7):
        w_start_repaint_square = 0
        b_start_repaint_square = 0

        for ii in range(8):
            for jj in range(8):

                if (j + jj) % 2 == 0:
                    if (i + ii) % 2 == 0:
                        if board[i + ii][j + jj] != "W":
                            w_start_repaint_square += 1
                    else:
                        if board[i + ii][j + jj] != "B":
                            w_start_repaint_square += 1
                else:
                    if (i + ii) % 2 == 0:
                        if board[i + ii][j + jj] != "B":
                            w_start_repaint_square += 1
                    else:
                        if board[i + ii][j + jj] != "W":
                            w_start_repaint_square += 1

                if (j + jj) % 2 == 0:
                    if (i + ii) % 2 == 0:
                        if board[i + ii][j + jj] != "B":
                            b_start_repaint_square += 1
                    else:
                        if board[i + ii][j + jj] != "W":
                            b_start_repaint_square += 1
                else:
                    if (i + ii) % 2 == 0:
                        if board[i + ii][j + jj] != "W":
                            b_start_repaint_square += 1
                    else:
                        if board[i + ii][j + jj] != "B":
                            b_start_repaint_square += 1

        answer = min(answer, w_start_repaint_square, b_start_repaint_square)
else:
    print(answer)
