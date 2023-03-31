from collections import deque
import sys

input = sys.stdin.readline

DY = [0, 0, -1, 1]
DX = [-1, 1, 0, 0]
WAY_COUNT = 4


def get_feed_list(baby_shark_i, baby_shark_j):
    feed_list = []

    shark_location_queue = deque()
    visit[baby_shark_i][baby_shark_j] = True
    shark_location_queue.append((baby_shark_i, baby_shark_j, 0, False))

    while shark_location_queue:
        i, j, move, is_eatable = shark_location_queue.popleft()

        if is_eatable:
            feed_list.append((move, i, j))

        for way in range(WAY_COUNT):
            next_i = i + DY[way]
            next_j = j + DX[way]

            if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
                continue

            if not visit[next_i][next_j] and space[next_i][next_j] <= baby_shark_weight:
                visit[next_i][next_j] = True

                if (
                    space[next_i][next_j] != 0
                    and space[next_i][next_j] < baby_shark_weight
                ):
                    shark_location_queue.append((next_i, next_j, move + 1, True))
                else:
                    shark_location_queue.append((next_i, next_j, move + 1, False))

    return feed_list


N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

baby_shark_grow_count = baby_shark_weight = 2
baby_shark_i = baby_shark_j = 0

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            baby_shark_i = i
            baby_shark_j = j
            space[baby_shark_i][baby_shark_j] = 0

answer = 0
while True:
    visit = [[False for _ in range(N)] for _ in range(N)]
    feed_list = get_feed_list(baby_shark_i, baby_shark_j)

    if feed_list:
        feed_list.sort()

        answer += feed_list[0][0]
        baby_shark_i = feed_list[0][1]
        baby_shark_j = feed_list[0][2]

        baby_shark_grow_count -= 1
        if baby_shark_grow_count == 0:
            baby_shark_weight += 1
            baby_shark_grow_count = baby_shark_weight

        space[baby_shark_i][baby_shark_j] = 0
    else:
        print(answer)
        break
