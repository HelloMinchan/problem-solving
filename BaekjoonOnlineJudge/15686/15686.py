import sys, copy
from sre_constants import CHCODES
input = sys.stdin.readline


def DFS(si):
    if len(stack) == M:
        closedChickenHouse.append(copy.deepcopy(stack))

    for i in range(si, len(chickenHouse)):
        if not visit[i]:
            visit[i] = True
            stack.append(chickenHouse[i])
            DFS(i + 1)
            visit[i] = False
            stack.pop()


N , M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chickenHouse = []
closedChickenHouse = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chickenHouse.append((i, j))

visit = [False] * len(chickenHouse)
stack = []
DFS(0)

minChickenDist = 2147483647
for closedChickenHouse_coord in closedChickenHouse:
    chickenDist = 0
    for house_coord in house:
        tempChickenDist = 2147483647

        for chickenHouse_coord in closedChickenHouse_coord:
            tempChickenDist = min(tempChickenDist, abs(chickenHouse_coord[0] - house_coord[0]) + abs(chickenHouse_coord[1] - house_coord[1]))
        
        chickenDist += tempChickenDist
        
    minChickenDist = min(minChickenDist, chickenDist)

print(minChickenDist)
