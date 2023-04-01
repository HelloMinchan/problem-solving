import sys

input = sys.stdin.readline

DY = [-1, -1, -1, 0, 0, 1, 1, 1]
DX = [-1, 0, 1, -1, 1, -1, 0, 1]
WAY_COUNT = 8


def spring_summer_winter():
    for i in range(N):
        for j in range(N):
            grow_trees = sorted(trees[i][j])[:]
            trees[i][j] = []
            dead_trees = []

            for age in grow_trees:
                if ground[i][j] >= age:
                    ground[i][j] -= age

                    trees[i][j].append(age + 1)
                else:
                    dead_trees.append(age)

            for age in dead_trees:
                ground[i][j] += age // 2

            ground[i][j] += A[i][j]


def fall():
    for i in range(N):
        for j in range(N):
            for age in trees[i][j]:
                if age % 5 == 0:
                    for way in range(WAY_COUNT):
                        next_i = i + DY[way]
                        next_j = j + DX[way]

                        if next_i < 0 or next_i > N - 1 or next_j < 0 or next_j > N - 1:
                            continue

                        trees[next_i][next_j].append(1)


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

trees = [[[] for _ in range(N)] for _ in range(N)]
dead_trees = [[[] for _ in range(N)] for _ in range(N)]
ground = [[5 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, z = map(int, input().split())

    trees[x - 1][y - 1].append(z)

for _ in range(K):
    spring_summer_winter()
    fall()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)
