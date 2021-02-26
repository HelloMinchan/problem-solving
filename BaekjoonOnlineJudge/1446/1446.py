import sys
input = sys.stdin.readline

N, D = map(int, input().split())

adjacentList = [{} for _ in range(10001)]

for _ in range(N):
    startVertex, destinationVertex, length = map(int, input().split())

    adjacentList[startVertex][destinationVertex] = min(length, adjacentList[startVertex].get(destinationVertex, 2147483647))

distance = list(range(10001))

for vertex in range(D+1):
    if vertex > 0:
        distance[vertex] = min(distance[vertex], distance[vertex-1] + 1)

    if len(adjacentList[vertex]):
        for shortcut in adjacentList[vertex].keys():
            distance[shortcut] = min(distance[shortcut], distance[vertex] + adjacentList[vertex][shortcut])

print(distance[D])