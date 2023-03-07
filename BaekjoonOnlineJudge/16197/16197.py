# 8:03 ~
from collections import deque
import sys

input = sys.stdin.readline

COIN = "o"
WALL = "#"
EMPTY = "."
WAY_COUNT = 4

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(dq):
    answer = 0

    while dq:
        answer += 1
        if answer == 11:
            return -1

        dq_count = len(dq)

        for _ in range(dq_count):
            location = dq.popleft()
            first_coin_i, first_coin_j = location[0]
            second_coin_i, second_coin_j = location[1]

            for way in range(WAY_COUNT):
                next_first_coin_i = first_coin_i + dx[way]
                next_first_coin_j = first_coin_j + dy[way]
                next_second_coin_i = second_coin_i + dx[way]
                next_second_coin_j = second_coin_j + dy[way]

                is_first_coin_out = False
                is_second_coin_out = False

                if (
                    next_first_coin_i < 0
                    or next_first_coin_i > N - 1
                    or next_first_coin_j < 0
                    or next_first_coin_j > M - 1
                ):
                    is_first_coin_out = True

                if (
                    next_second_coin_i < 0
                    or next_second_coin_i > N - 1
                    or next_second_coin_j < 0
                    or next_second_coin_j > M - 1
                ):
                    is_second_coin_out = True

                if is_first_coin_out and is_second_coin_out:
                    continue
                elif not is_first_coin_out and not is_second_coin_out:
                    if (
                        not first_visit[next_first_coin_i][next_first_coin_j][
                            next_second_coin_i
                        ][next_second_coin_j]
                        or not second_visit[next_second_coin_i][next_second_coin_j][
                            next_first_coin_i
                        ][next_first_coin_j]
                    ):
                        first_visit[next_first_coin_i][next_first_coin_j][
                            next_second_coin_i
                        ][next_second_coin_j] = True
                        second_visit[next_second_coin_i][next_second_coin_j][
                            next_first_coin_i
                        ][next_first_coin_j] = True

                        location = []
                        if board[next_first_coin_i][next_first_coin_j] in [
                            EMPTY,
                            COIN,
                        ] and board[next_second_coin_i][next_second_coin_j] in [
                            EMPTY,
                            COIN,
                        ]:
                            location.append((next_first_coin_i, next_first_coin_j))
                            location.append((next_second_coin_i, next_second_coin_j))
                        elif board[next_first_coin_i][next_first_coin_j] in [
                            EMPTY,
                            COIN,
                        ]:
                            location.append((next_first_coin_i, next_first_coin_j))
                            location.append((second_coin_i, second_coin_j))
                        elif board[next_second_coin_i][next_second_coin_j] in [
                            EMPTY,
                            COIN,
                        ]:
                            location.append((first_coin_i, first_coin_j))
                            location.append((next_second_coin_i, next_second_coin_j))

                        if location:
                            dq.append(location)
                else:
                    return answer

    return -1


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
first_visit = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]
second_visit = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]

dq = deque()
location = []

for i in range(N):
    for j in range(M):
        if board[i][j] == COIN:
            location.append((i, j))

first_visit[location[0][0]][location[0][1]][location[1][0]][location[1][1]] = True
second_visit[location[1][0]][location[1][1]][location[0][0]][location[0][1]] = True
dq.append(location)

print(bfs(dq))
