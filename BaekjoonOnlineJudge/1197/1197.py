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

    for w, sv, dv in adjList:
        if union(sv, dv):
            ans += w


V, E = map(int, input().split())
ans = 0

disjointSet = [x for x in range(V + 1)]

adjList = []
for _ in range(E):
    A, B, C = map(int, input().split())

    adjList.append((C, A, B))

adjList.sort()

kruskal()

print(ans)
