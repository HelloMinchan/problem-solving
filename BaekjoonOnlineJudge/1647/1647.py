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
        return False

    if findSV < findDV:
        disjointSet[findDV] = findSV
    else:
        disjointSet[findSV] = findDV

    return True


def kruskal():
    global ans

    count = 0
    for w, sv, dv in roads:
        if union(sv, dv):
            count += 1

            if count < N - 1:
                ans += w


N, M = map(int, input().split())

ans = 0
disjointSet = [x for x in range(N + 1)]

roads = []
for _ in range(M):
    A, B, C = map(int, input().split())

    roads.append((C, A, B))
    roads.append((C, B, A))

roads.sort()

kruskal()

print(ans)
