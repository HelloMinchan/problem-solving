import sys

input = sys.stdin.readline

BLACK_ROCK = 1
WHITE_ROCK = 2
N = 19

dy = [0, 1, 1, -1]
dx = [1, 0, 1, 1]
WAY_COUNT = 4


def bfs(start_i, start_j, start_rock):
    for way in range(WAY_COUNT):
        count = 1
        next_i = start_i + dy[way]
        next_j = start_j + dx[way]

        while (
            0 <= next_i < N and 0 <= next_j < N and board[next_i][next_j] == start_rock
        ):
            count += 1

            if count == 5:
                # 한 칸 이전 육목 체크
                if (
                    0 <= start_i - dy[way] < N
                    and 0 <= start_j - dx[way] < N
                    and board[start_i - dy[way]][start_j - dx[way]] == start_rock
                ):
                    break

                # 한 칸 이후 육목 체크
                if (
                    0 <= next_i + dy[way] < N
                    and 0 <= next_j + dx[way] < N
                    and board[next_i + dy[way]][next_j + dx[way]] == start_rock
                ):
                    break

                print(start_rock)
                print(start_i + 1, start_j + 1)
                sys.exit(0)

            next_i += dy[way]
            next_j += dx[way]


board = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] in [BLACK_ROCK, WHITE_ROCK]:
            bfs(i, j, board[i][j])

print(0)
