import sys
from collections import deque

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
WAY_COUNT = 4


def rotate_board(query):
    global board

    x1, y1, x2, y2 = query

    i = x1
    j = y1
    minimum_number = sys.maxsize
    number_queue = deque()
    for way in range(WAY_COUNT):
        while x1 <= i <= x2 and y1 <= j <= y2:
            number_queue.append(board[i][j])
            minimum_number = min(minimum_number, board[i][j])
            i += dy[way]
            j += dx[way]

        i -= dy[way]
        j -= dx[way]
        if way + 1 < WAY_COUNT:
            i += dy[way + 1]
            j += dx[way + 1]

    i = x1
    j = y1
    number_queue.rotate(1)
    for way in range(WAY_COUNT):
        while x1 <= i <= x2 and y1 <= j <= y2:
            board[i][j] = number_queue.popleft()
            i += dy[way]
            j += dx[way]

        i -= dy[way]
        j -= dx[way]
        if way + 1 < WAY_COUNT:
            i += dy[way + 1]
            j += dx[way + 1]

    return minimum_number


def solution(N, M, queries):
    global board
    board = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            board[i][j] = (i - 1) * M + j

    answer = []
    for query in queries:
        answer.append(rotate_board(query))

    return answer
