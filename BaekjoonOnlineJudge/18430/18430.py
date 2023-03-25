import sys

input = sys.stdin.readline

dy = [(0, 1), (-1, 0), (-1, 0), (0, 1)]
dx = [(-1, 0), (0, -1), (0, 1), (1, 0)]
WAY_COUNT = 4


def is_valid_index(i, j):
    if i < 0 or i > N - 1 or j < 0 or j > M - 1:
        return False
    return True


def dfs(i, j, total_strength):
    global answer

    if j == M:
        j = 0
        i += 1

    if i == N:
        answer = max(answer, total_strength)
        return

    if not visit[i][j]:
        for way in range(WAY_COUNT):
            left_i = i + dy[way][0]
            left_j = j + dx[way][0]
            right_i = i + dy[way][1]
            right_j = j + dx[way][1]

            if (
                is_valid_index(left_i, left_j)
                and is_valid_index(right_i, right_j)
                and not visit[left_i][left_j]
                and not visit[right_i][right_j]
            ):
                visit[i][j] = True
                visit[left_i][left_j] = True
                visit[right_i][right_j] = True
                dfs(
                    i,
                    j + 1,
                    total_strength
                    + (board[i][j] * 2)
                    + board[left_i][left_j]
                    + board[right_i][right_j],
                )
                visit[i][j] = False
                visit[left_i][left_j] = False
                visit[right_i][right_j] = False

    dfs(i, j + 1, total_strength)


N, M = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

visit = [[False for _ in range(M)] for _ in range(N)]

answer = 0

dfs(0, 0, 0)

print(answer)
