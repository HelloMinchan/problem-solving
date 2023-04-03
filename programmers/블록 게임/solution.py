def try_break_block(start_i, start_j):
    for i in range(start_i):
        if board[i][start_j]:
            return False

    return True


def find(start_i, start_j, i_length, j_length):
    empty_count = 0
    before_block_type = -1

    for i in range(start_i, start_i + i_length):
        for j in range(start_j, start_j + j_length):
            if board[i][j] == 0:
                if not try_break_block(i, j):
                    return False

                empty_count += 1

                if empty_count > 2:
                    return False
            else:
                if before_block_type == -1:
                    before_block_type = board[i][j]
                else:
                    if before_block_type != board[i][j]:
                        return False

    for i in range(start_i, start_i + i_length):
        for j in range(start_j, start_j + j_length):
            board[i][j] = 0

    return True


def solution(parameter_board):
    global board
    board = parameter_board

    n = len(board)
    answer = 0

    while True:
        broken_count = 0

        for i in range(n):
            for j in range(n):
                if i <= n - 2 and j <= n - 3 and find(i, j, 2, 3):
                    broken_count += 1
                elif i <= n - 3 and j <= n - 2 and find(i, j, 3, 2):
                    broken_count += 1

        if broken_count:
            answer += broken_count
        else:
            break

    return answer
