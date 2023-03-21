from collections import deque, defaultdict
import sys

input = sys.stdin.readline


def bfs(union, visit, union_number, i, j):
    dq = deque()
    visit[i][j] = True
    union[i][j] = union_number
    dq.append((i, j))

    union_count = 0
    union_population = 0

    while dq:
        i, j = dq.popleft()
        union_count += 1
        union_population += ground[i][j]

        for way in range(WAY_COUNT):
            next_i = i + dy[way]
            next_j = j + dx[way]

            if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
                continue
            if (
                not visit[next_i][next_j]
                and L <= abs(ground[i][j] - ground[next_i][next_j]) <= R
            ):
                visit[next_i][next_j] = True
                union[next_i][next_j] = union_number
                dq.append((next_i, next_j))

    return union_count, union_population


def transfer_population():
    answer_day = -1
    is_transfer = False

    while answer_day == -1 or is_transfer:
        is_transfer = False
        answer_day += 1

        union = [[-1 for _ in range(N)] for _ in range(N)]

        union_number = 1
        visit = [[False for _ in range(N)] for _ in range(N)]
        union_population_dict = defaultdict(int)
        union_number_set = set()
        for i in range(N):
            for j in range(N):
                if not visit[i][j]:
                    union_count, union_population = bfs(
                        union, visit, union_number, i, j
                    )

                    if union_count >= 2:
                        is_transfer = True
                        union_number_set.add(union_number)
                        union_population_dict[union_number] = (
                            union_population // union_count
                        )
                    union_number += 1

        for i in range(N):
            for j in range(N):
                if union[i][j] in union_number_set:
                    ground[i][j] = union_population_dict[union[i][j]]

    return answer_day


N, L, R = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
WAY_COUNT = 4

print(transfer_population())
