import sys
input = sys.stdin.readline


def find(target):
    if target == citys[target]:
        return target
    citys[target] = find(citys[target])
    return citys[target]


def union(A, B):
    A = find(A)
    B = find(B)

    if A < B:
        citys[B] = A
    else:
        citys[A] = B


N = int(input())
M = int(input())
citys = [ i for i in range(N + 1)]

for i in range(N):
    connectedCity = list(map(int, input().split()))

    for j in range(N):
        if connectedCity[j]:
            union(i + 1, j + 1)

plannedCities = list(map(int, input().split()))

isPossible = "YES"
beforeFindCity = 0

for i, city in enumerate(plannedCities):
    findCity = find(city)
    if not i:
        beforeFindCity = findCity
        continue
    if beforeFindCity != find(city):
        isPossible = "NO"
        break
    beforeFindCity = findCity

print(isPossible)