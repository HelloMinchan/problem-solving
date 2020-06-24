import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


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


T = int(input())

for _ in range(T):
    N = int(input())
    sequence = [0] + list(map(int, input().split()))
    disjointSet = [x for x in range(N + 1)]

    for sv, dv in enumerate(sequence):
        if not sv:
            continue

        union(sv, dv)

    for i in range(1, N + 1):
        find(i)

    print(len(set(disjointSet[1:])))
