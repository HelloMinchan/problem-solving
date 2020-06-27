import sys
input = sys.stdin.readline


def find(target):
    if airport[target] == target:
        return target
    
    airport[target] = find(airport[target])
    return airport[target]


def union(a, b):
    findA = find(a)
    findB = find(b)
    
    airport[findA] = findB


def doking():
    count = 0

    for ap in airplanes:
        if not find(ap):
            break
        
        union(ap, find(ap) - 1)
        count += 1

    return count


G = int(input())
P = int(input())

airport = list(range(G + 1))
airplanes = [int(input()) for _ in range(P)]

print(doking())
