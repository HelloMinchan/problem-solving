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

    for w, sv, dv in tunnel:
        if union(sv, dv):
            ans += w


N = int(input())

ans = 0
disjointSet = [x for x in range(N)]

coords = [list(map(int, input().split())) for _ in range(N)]

tunnel = []
for i in range(N):
    for j in range(i + 1, N):
        dist = min(abs(coords[i][0] - coords[j][0]), abs(coords[i][1] - coords[j][1]), abs(coords[i][2] - coords[j][2]))

        tunnel.append((dist, i, j))

tunnel.sort()

kruskal()

print(ans)
