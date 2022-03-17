import sys, heapq

input = sys.stdin.readline


def find(target):
    if target == disjoint_set[target]:
        return target
    
    disjoint_set[target] = find(disjoint_set[target])
    return disjoint_set[target]


def union(a, b):
    find_a = find(a)
    find_b = find(b)

    if find_a == find_b:
        return False
    elif find_a < find_b:
        disjoint_set[find_b] = find_a
    else:
        disjoint_set[find_a] = find_b

    return True

def kruskal():
    global answer

    while hq:
        weight, a, b = heapq.heappop(hq)
    
        if union(a, b):
            answer += weight

V, E = map(int, input().split())
disjoint_set = list(range(V+1))
answer = 0

hq = []

for _ in range(E):
    A, B, C = map(int, input().split())

    heapq.heappush(hq, (C, A, B))

kruskal()

print(answer)