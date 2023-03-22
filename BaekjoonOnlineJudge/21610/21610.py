import sys

input = sys.stdin.readline

dy = [0] + [0, -1, -1, -1, 0, 1, 1, 1]
dx = [0] + [-1, -1, 0, 1, 1, 1, 0, -1]


def get_around_water_count(i, j):
    water_count = 0

    for way in [2, 4, 6, 8]:
        next_i = i + dy[way]
        next_j = j + dx[way]

        if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
            continue

        if bucket[next_i][next_j] > 0:
            water_count += 1

    return water_count


N, M = map(int, input().split())

bucket = [list(map(int, input().split())) for _ in range(N)]

cloud_location = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for _ in range(M):
    way, move = map(int, input().split())
    visit = [[False for _ in range(N)] for _ in range(N)]

    for cloud_index in range(len(cloud_location)):
        i, j = cloud_location[cloud_index]

        cloud_location[cloud_index][0] = i + dy[way] * move
        cloud_location[cloud_index][1] = j + dx[way] * move

        if cloud_location[cloud_index][0] < 0:
            cloud_location[cloud_index][0] = N - abs(cloud_location[cloud_index][0]) % N

        if cloud_location[cloud_index][0] > 0:
            cloud_location[cloud_index][0] = cloud_location[cloud_index][0] % N

        if cloud_location[cloud_index][1] < 0:
            cloud_location[cloud_index][1] = N - abs(cloud_location[cloud_index][1]) % N

        if cloud_location[cloud_index][1] > 0:
            cloud_location[cloud_index][1] = cloud_location[cloud_index][1] % N

        bucket[cloud_location[cloud_index][0]][cloud_location[cloud_index][1]] += 1

    for cloud_index in range(len(cloud_location)):
        visit[cloud_location[cloud_index][0]][cloud_location[cloud_index][1]] = True
        bucket[cloud_location[cloud_index][0]][
            cloud_location[cloud_index][1]
        ] += get_around_water_count(
            cloud_location[cloud_index][0], cloud_location[cloud_index][1]
        )

    cloud_location = []
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if bucket[i][j] >= 2:
                    cloud_location.append([i, j])
                    bucket[i][j] -= 2

answer = 0
for row in bucket:
    answer += sum(row)
print(answer)
