import sys

input = sys.stdin.readline


def try_attach_sticker(i, j, sticker_location):
    for location in sticker_location:
        next_i = i + location[0]
        next_j = j + location[1]

        if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > M - 1:
            return False

        if notebook[next_i][next_j]:
            return False

    return True


def real_attach_sticker(i, j, sticker_location):
    for location in sticker_location:
        next_i = i + location[0]
        next_j = j + location[1]

        notebook[next_i][next_j] = True


def preprocess_location(locations):
    min_i = min([location[0] for location in locations])
    min_j = min([location[1] for location in locations])

    for location in locations:
        location[0] -= min_i
        location[1] -= min_j

    return locations


def rotate_location(sticker_location):
    rotated_location = []
    for location in sticker_location:
        rotated_location.append([location[1], C - 1 - location[0]])

    return preprocess_location(rotated_location)


def attach_sticker(sticker_location):
    now_sticker_location = sticker_location

    for _ in range(4):
        for i in range(N):
            for j in range(M):
                if try_attach_sticker(i, j, now_sticker_location):
                    real_attach_sticker(i, j, now_sticker_location)
                    return

        now_sticker_location = rotate_location(now_sticker_location)[:]


N, M, K = map(int, input().split())

notebook = [[False for _ in range(M)] for _ in range(N)]

for _ in range(K):
    R, C = map(int, input().split())

    sticker = [list(map(int, input().split())) for _ in range(R)]

    sticker_location = []
    for i in range(R):
        for j in range(C):
            if sticker[i][j] == 1:
                sticker_location.append([i, j])

    attach_sticker(sticker_location)

answer = 0
for row in notebook:
    answer += sum(row)

print(answer)
