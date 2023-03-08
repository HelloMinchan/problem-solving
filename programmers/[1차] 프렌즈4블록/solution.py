from collections import deque

dx = [1, 0, 1]
dy = [0, -1, -1]
WAY_COUNT = 3
DELETED = "0"


def check_2_by_2_squre(board, m, n):
    delete_location = set()

    for i in range(m):
        for j in range(n):
            block_type = board[i][j]

            if block_type == DELETED:
                continue

            candidate_location = [(i, j)]
            for way in range(WAY_COUNT):
                next_i = i + dx[way]
                next_j = j + dy[way]
                candidate_location.append((next_i, next_j))

                if next_i < 0 or next_i > m - 1 or next_j < 0 or next_j > n - 1:
                    break

                if board[next_i][next_j] != block_type:
                    break
            else:
                for location in candidate_location:
                    delete_location.add(location)

    return delete_location


def delete_block(board, delete_location):
    for location in delete_location:
        i, j = location

        board[i][j] = DELETED


def relocate_board(board, m, n):
    for j in range(n):
        dq = deque()

        for i in range(m - 1, -1, -1):
            block_type = board[i][j]

            if block_type != DELETED:
                dq.append(block_type)

        for i in range(m - 1, -1, -1):
            if dq:
                board[i][j] = dq.popleft()
            else:
                board[i][j] = DELETED


def solution(m, n, board):
    answer = 0

    game_board = []
    for line in board:
        game_board.append(list(line))

    while True:
        delete_location = check_2_by_2_squre(game_board, m, n)

        if delete_location:
            answer += len(delete_location)
            delete_block(game_board, delete_location)
            relocate_board(game_board, m, n)
        else:
            break

    return answer
