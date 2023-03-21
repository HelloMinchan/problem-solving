import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
WAY_COUNT = 4


def get_around_like_count(student, i, j):
    like_count = 0

    for way in range(WAY_COUNT):
        next_i = i + dy[way]
        next_j = j + dx[way]

        if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
            continue

        if seat_room[next_i][next_j] in student[1:]:
            like_count += 1

    return like_count


N = int(input())
students = []
for _ in range(N * N):
    students.append(list(map(int, input().split())))

class_room = [[0 for _ in range(N)] for _ in range(N)]
seat_room = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        adj_count = 0

        for way in range(WAY_COUNT):
            next_i = i + dy[way]
            next_j = j + dx[way]

            if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
                continue

            adj_count += 1

        class_room[i][j] = adj_count

for student in students:
    target_like_count = 0
    target_count = 0
    target_i = 0
    target_j = 0

    for i in range(N):
        is_found_target = False
        for j in range(N):
            if seat_room[i][j] == 0:
                target_i = i
                target_j = j
                is_found_target = True
                break
        if is_found_target:
            break

    for i in range(N):
        for j in range(N):
            if seat_room[i][j] == 0:
                around_like_count = get_around_like_count(student, i, j)

                if target_like_count < around_like_count:
                    target_like_count = around_like_count
                    target_count = class_room[i][j]
                    target_i = i
                    target_j = j
                elif (
                    around_like_count == target_like_count
                    and target_count < class_room[i][j]
                ):
                    target_count = class_room[i][j]
                    target_i = i
                    target_j = j

    seat_room[target_i][target_j] = student[0]

    for way in range(WAY_COUNT):
        next_target_i = target_i + dy[way]
        next_target_j = target_j + dx[way]

        if (
            next_target_i < 0
            or next_target_i > N - 1
            or next_target_j < 0
            or next_target_j > N - 1
        ):
            continue

        class_room[next_target_i][next_target_j] -= 1

students.sort(key=lambda student: student[0])

answer = 0
for i in range(N):
    for j in range(N):
        like_count = 0

        for way in range(WAY_COUNT):
            next_i = i + dy[way]
            next_j = j + dx[way]

            if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
                continue

            if seat_room[next_i][next_j] in students[seat_room[i][j] - 1][1:]:
                like_count += 1

        if like_count == 0:
            answer += 0
        elif like_count == 1:
            answer += 1
        elif like_count == 2:
            answer += 10
        elif like_count == 3:
            answer += 100
        else:
            answer += 1000

print(answer)
