import sys
input = sys.stdin.readline


def find(target):
    if disjointSet[target] == target:
        return target
    
    disjointSet[target] = find(disjointSet[target])
    return disjointSet[target]


def union(sv, dv):
    findSV = find(sv)
    findDV = find(dv)

    if findSV == findDV:
        return
    
    if findSV < findDV:
        disjointSet[findDV] = findSV
    else:
        disjointSet[findSV] = findDV


N = int(input())
M = int(input())

disjointSet = list(range(N + 1))
adjList = []

for _ in range(M):
    sv, dv = map(int, input().split())

    adjList.append((sv, dv))

for sv, dv in adjList:
    union(sv, dv)

for i in range(1, N + 1):
    find(i)
    
print(disjointSet[2:].count(1))
