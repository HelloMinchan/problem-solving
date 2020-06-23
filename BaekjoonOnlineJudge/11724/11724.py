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


N, M = map(int, input().split())

disjointSet = [x for x in range(N + 1)]

connection = []
for _ in range(M):
    sv, dv = map(int, input().split())

    connection.append((sv, dv))

for sv, dv in connection:
    union(sv, dv)

for i in range(N + 1):
    find(i)

print(len(set(disjointSet[1:])))
