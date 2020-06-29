import sys, math
input = sys.stdin.readline


def find(target):
    if starSign[target] == target:
        return target
    
    starSign[target] = find(starSign[target])
    return starSign[target]


def union(sv, dv):
    findSV = find(sv)
    findDV = find(dv)

    if findSV == findDV:
        return False
    
    if findSV < findDV:
        starSign[findDV] = findSV
    else:
        starSign[findSV] = findDV
    
    return True


def kruskal():
    global cost

    for w, sv, dv in starDist:
        if union(sv, dv):
            cost += w


n = int(input())

cost = 0
starSign = list(range(n))
starLocation = []
for _ in range(n):
    starLocation.append(list(map(float, input().split())))

starDist = []
for i in range(n - 1):
    for j in range(i + 1, n):
        w = math.sqrt((starLocation[i][0] - starLocation[j][0]) ** 2 + (starLocation[i][1] - starLocation[j][1]) ** 2)
        starDist.append((w, i, j))

starDist.sort()

kruskal()

print("%.2f" % cost)
