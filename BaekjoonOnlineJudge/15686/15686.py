import sys
input = sys.stdin.readline
from itertools import combinations as C

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
allHouse = []
allChicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            allHouse.append((i, j))
        elif arr[i][j] == 2:
            allChicken.append((i, j))

allAliveChickenList = list(C(allChicken, M))

solution = []
for aliveChickenList in allAliveChickenList:
    allDistance = 0
    for house in allHouse:
        distance = 9999
        for chickenX, chickenY in aliveChickenList:
            if distance > abs(house[0] - chickenX) + abs(house[1] - chickenY):
                distance = abs(house[0] - chickenX) + abs(house[1] - chickenY)
        allDistance += distance
    solution.append(allDistance)

print(min(solution))