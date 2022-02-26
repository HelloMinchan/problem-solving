import sys

input = sys.stdin.readline

N = int(input())

house = []
for _ in range(N):
    house.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(3):
        if j == 0:
            house[i][j] += min(house[i - 1][j + 1], house[i - 1][j + 2])
        elif j == 1:
            house[i][j] += min(house[i - 1][j - 1], house[i - 1][j + 1])
        else:
            house[i][j] += min(house[i - 1][j - 1], house[i - 1][j - 2])

print(min(house[N - 1]))
