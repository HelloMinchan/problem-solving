import sys

input = sys.stdin.readline

N = int(input())

houses = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            houses[i][j] += min(houses[i-1][1], houses[i-1][2])
        elif j == 1:
            houses[i][j] += min(houses[i-1][0], houses[i-1][2])
        else:
            houses[i][j] += min(houses[i-1][0], houses[i-1][1])

print(min(houses[-1]))