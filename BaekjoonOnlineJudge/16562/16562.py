import sys
input = sys.stdin.readline


def find(target):
    if network[target] == target:
        return target
    
    network[target] = find(network[target])
    return network[target]


def union(a, b):
    findA = find(a)
    findB = find(b)

    if findA == findB:
        return
    
    if findA < findB:
        network[findB] = findA
    else:
        network[findA] = findB


N, M, k = map(int, input().split())
costs = [0] + list(map(int, input().split()))

network = list(range(N + 1))

for _ in range(M):
    a, b = map(int, input().split())

    union(a, b)

for i in range(1, N + 1):
    find(i)

INF = 2147483647
cheapList = [INF] * (N + 1)
for i in range(1, N + 1):
    cheapList[network[i]] = min(cheapList[network[i]], costs[i])

friendFee = 0
for fee in cheapList:
    if fee != INF:
        friendFee += fee

if friendFee <= k:
    print(friendFee)
else:
    print("Oh no")
