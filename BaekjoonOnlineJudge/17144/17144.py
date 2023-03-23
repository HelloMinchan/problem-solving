from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
WAY_COUNT = 4
AIR_CONDITIONER = -1


def diffuse_dust():
    dust_position_queue = deque()

    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                diffusion_count = 0

                for way in range(WAY_COUNT):
                    next_i = i + dy[way]
                    next_j = j + dx[way]

                    if (
                        next_i < 0
                        or next_i > R - 1
                        or next_j < 0
                        or next_j > C - 1
                        or (next_i, next_j) in airconditioner_position
                    ):
                        continue
                    diffusion_count += 1

                dust_position_queue.append((i, j, room[i][j], diffusion_count))

    dust_diffusion_queue = deque()
    for dust_position in dust_position_queue:
        i, j, _, _ = dust_position
        diffusion_amount = room[i][j] // 5

        for way in range(WAY_COUNT):
            next_i = i + dy[way]
            next_j = j + dx[way]

            if (
                next_i < 0
                or next_i > R - 1
                or next_j < 0
                or next_j > C - 1
                or (next_i, next_j) in airconditioner_position
            ):
                continue

            dust_diffusion_queue.append((next_i, next_j, diffusion_amount))

    while dust_diffusion_queue:
        i, j, diffusion_amount = dust_diffusion_queue.popleft()

        room[i][j] += diffusion_amount

    while dust_position_queue:
        i, j, origin_dust_amout, diffusion_count = dust_position_queue.popleft()

        room[i][j] -= (origin_dust_amout // 5) * diffusion_count


def blow_wind(airconditioner_position, wind_way):
    i, j = airconditioner_position

    dust_amount_queue = deque()
    for way in wind_way:
        while (
            i + dy[way] >= 0
            and i + dy[way] <= R - 1
            and j + dx[way] >= 0
            and j + dx[way] <= C - 1
            and (i + dy[way], j + dx[way]) != airconditioner_position
        ):
            i = i + dy[way]
            j = j + dx[way]

            dust_amount_queue.append(room[i][j])

    i, j = airconditioner_position
    j = j + 1
    room[i][j] = 0

    for way in wind_way:
        while (
            i + dy[way] >= 0
            and i + dy[way] <= R - 1
            and j + dx[way] >= 0
            and j + dx[way] <= C - 1
            and (i + dy[way], j + dx[way]) != airconditioner_position
        ):
            i = i + dy[way]
            j = j + dx[way]

            room[i][j] = dust_amount_queue.popleft()


def execute_airconditioner():
    up_airconditioner_position, down_airconditioner_position = airconditioner_position

    blow_wind(up_airconditioner_position, [3, 0, 2, 1])
    blow_wind(down_airconditioner_position, [3, 1, 2, 0])


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

airconditioner_position = []
for i in range(R):
    for j in range(C):
        if room[i][j] == AIR_CONDITIONER:
            airconditioner_position.append((i, j))

for _ in range(T):
    diffuse_dust()
    execute_airconditioner()


answer = 0
for i in range(R):
    for j in range(C):
        if (i, j) not in airconditioner_position:
            answer += room[i][j]

print(answer)
