def diffusion():
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                cnt = 0
                for way in range(4):
                    ii = i + dx[way]
                    jj = j + dy[way]
                    if ii < 0 or ii > R - 1 or jj < 0 or jj > C - 1:
                        continue
                    if room[i][j] < 5:
                        continue
                    if (ii, jj) == (air_cleaner[0], 0) or (ii, jj) == (
                        air_cleaner[1],
                        0,
                    ):
                        continue

                    after_action_room[ii][jj] = (
                        after_action_room[ii][jj] + room[i][j] // 5
                    )
                    cnt = cnt + 1
                after_action_room[i][j] = (
                    after_action_room[i][j] + room[i][j] - room[i][j] // 5 * cnt
                )


def active_air_cleaner():
    for i in range(air_cleaner[0] - 2, -1, -1):
        after_action_room[i + 1][0] = after_action_room[i][0]
    for i in range(1, C):
        after_action_room[0][i - 1] = after_action_room[0][i]
    for i in range(1, air_cleaner[0] + 1):
        after_action_room[i - 1][-1] = after_action_room[i][-1]
    for i in range(C - 2, 0, -1):
        after_action_room[air_cleaner[0]][i + 1] = after_action_room[air_cleaner[0]][i]
    after_action_room[air_cleaner[0]][1] = 0

    for i in range(air_cleaner[1] + 2, R):
        after_action_room[i - 1][0] = after_action_room[i][0]
    for i in range(1, C):
        after_action_room[-1][i - 1] = after_action_room[-1][i]
    for i in range(R - 2, air_cleaner[1] - 1, -1):
        after_action_room[i + 1][-1] = after_action_room[i][-1]
    for i in range(C - 2, 0, -1):
        after_action_room[air_cleaner[1]][i + 1] = after_action_room[air_cleaner[1]][i]
    after_action_room[air_cleaner[1]][1] = 0


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]

air_cleaner = []
for i in range(R):
    if room[i][0] == -1:
        air_cleaner.append(i)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

after_action_room = [[0] * C for _ in range(R)]
diffusion()
active_air_cleaner()

for _ in range(T - 1):
    room = after_action_room.copy()
    after_action_room = [[0] * C for _ in range(R)]
    diffusion()
    active_air_cleaner()

answer = 0
for i in range(R):
    for j in range(C):
        if after_action_room[i][j] > 0:
            answer = answer + after_action_room[i][j]

print(answer)
