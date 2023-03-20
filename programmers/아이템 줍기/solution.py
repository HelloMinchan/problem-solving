from collections import deque

MAX_LENGTH = 51 * 2
board = [[False for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)]
visit = [[False for _ in range(MAX_LENGTH)] for _ in range(MAX_LENGTH)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
WAY_COUNT = 4


def fill_rectangles_in_board(rectangles):
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                board[i][j] = True


def delete_rectangles_inside_in_board(rectangles):
    for rectangle in rectangles:
        x1, y1, x2, y2 = rectangle
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2

        for i in range(y1 + 1, y2):
            for j in range(x1 + 1, x2):
                board[i][j] = False


def bfs(characterX, characterY, itemX, itemY):
    location_dq = deque()
    visit[characterY][characterX] = True
    location_dq.append((0, characterY, characterX))

    while location_dq:
        move, i, j = location_dq.popleft()

        if i == itemY and j == itemX:
            return move // 2

        for way in range(WAY_COUNT):
            next_i = i + dy[way]
            next_j = j + dx[way]

            if (
                next_i < 0
                or next_i > MAX_LENGTH - 1
                or next_j < 0
                or next_j > MAX_LENGTH - 1
            ):
                continue

            if not visit[next_i][next_j] and board[next_i][next_j]:
                visit[next_i][next_j] = True
                location_dq.append((move + 1, next_i, next_j))


def solution(rectangles, characterX, characterY, itemX, itemY):
    fill_rectangles_in_board(rectangles)
    delete_rectangles_inside_in_board(rectangles)

    return bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2)
