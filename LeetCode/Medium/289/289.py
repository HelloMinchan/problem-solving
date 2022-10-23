# 4:40 ~ 5:10

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def check_life(board, i, j):
    global N, M

    live_count = 0
    dead_count = 0

    for way in range(8):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
            continue

        if board[ii][jj] == 1:
            live_count += 1
        else:
            dead_count += 1

    if board[i][j] == 1:
        if live_count < 2:
            return 0
        elif live_count in [2, 3]:
            return 1
        else:
            return 0
    else:
        if live_count == 3:
            return 1
        else:
            return 0


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        global N, M

        N = len(board)
        M = len(board[0])

        new_board = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            for j in range(M):
                new_board[i][j] = check_life(board, i, j)

        for i in range(N):
            for j in range(M):
                board[i][j] = new_board[i][j]
