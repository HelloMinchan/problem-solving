import sys, heapq
input = sys.stdin.readline

def find(target):
    if disjointSet[target] == target:
        return target
    
    disjointSet[target] = find(disjointSet[target])
    return disjointSet[target]

def union(a, b):
    findA = find(a)
    findB = find(b)

    if findA == findB:
        return False
    
    if findA < findB:
        disjointSet[findB] = findA
    else:
        disjointSet[findA] = findB

    return True

def kruskal():
    global minimumCost
    
    while hq:
        cost, startVertex, destinationVertex = heapq.heappop(hq)

        if union(startVertex, destinationVertex):
            minimumCost += cost


N = int(input())
M = int(input())

disjointSet = list(range(N+1))
adjacentList = [[] for _ in range(N+1)]

for _ in range(M):
    startVertex, destinationVertex, cost = map(int, input().split())
    adjacentList[startVertex].append((destinationVertex, cost))
    adjacentList[destinationVertex].append((startVertex, cost))

minimumCost = 0

hq = []
for startVertex in range(N+1):
    for destinationVertex, cost in adjacentList[startVertex]:
        heapq.heappush(hq, (cost, startVertex, destinationVertex))

kruskal()

print(minimumCost)