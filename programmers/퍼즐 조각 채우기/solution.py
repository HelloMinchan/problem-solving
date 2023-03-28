from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
WAY_COUNT = 4


def preprocess_blocks(blocks):
    first_i = min([block[0] for block in blocks])
    first_j = min([block[1] for block in blocks])

    for block in blocks:
        block[0] -= first_i
        block[1] -= first_j

    return blocks


def rotate(block, length):
    rotated_block = []
    for i, j in block:
        rotated_block.append([j, length - 1 - i])

    return preprocess_blocks(rotated_block)


def bfs(matrix, i, j, target):
    global visit

    matrix_length = len(matrix)

    blocks = []
    location_queue = deque()
    visit[i][j] = True
    location_queue.append((i, j))

    while location_queue:
        i, j = location_queue.popleft()
        blocks.append([i, j])

        for way in range(WAY_COUNT):
            next_i = i + dy[way]
            next_j = j + dx[way]

            if (
                next_i < 0
                or next_i > matrix_length - 1
                or next_j < 0
                or next_j > matrix_length - 1
            ):
                continue

            if not visit[next_i][next_j] and matrix[next_i][next_j] == target:
                visit[next_i][next_j] = True
                location_queue.append((next_i, next_j))

    return blocks


def solution(game_board, table):
    global visit

    game_board_length = len(game_board)
    visit = [
        [False for _ in range(game_board_length)] for _ in range(game_board_length)
    ]

    blank_blocks = []
    for i in range(game_board_length):
        for j in range(game_board_length):
            if not visit[i][j] and game_board[i][j] == 0:
                blank_blocks.append(preprocess_blocks(bfs(game_board, i, j, 0)))

    table_length = len(table)
    visit = [[False for _ in range(table_length)] for _ in range(table_length)]

    blocks = []
    for i in range(table_length):
        for j in range(table_length):
            if not visit[i][j] and table[i][j] == 1:
                blocks.append(bfs(table, i, j, 1))

    answer = 0
    used_blocks = [False for _ in range(len(blocks))]

    for blank_block in blank_blocks:
        for i in range(len(blocks)):
            if not used_blocks[i]:
                now_block = blocks[i]
                for _ in range(4):
                    now_block = rotate(now_block, table_length)[:]

                    if sorted(blank_block) == sorted(now_block):
                        answer += len(blank_block)
                        used_blocks[i] = True
                        break

                if used_blocks[i]:
                    break

    return answer
