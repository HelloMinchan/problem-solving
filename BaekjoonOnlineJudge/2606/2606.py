import sys

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
        return
    elif find_a < find_b:
        disjoint_set[find_b] = find_a
    else:
        disjoint_set[find_a] = find_b

N = int(input())
edge = int(input())

adj_list = [[] for _ in range(N+1)]
disjoint_set = list(range(N+1))

for _ in range(edge):
    sv, dv = map(int, input().split())

    union(sv, dv)

for i in range(1, N+1):
    find(i)

print(disjoint_set[2:].count(disjoint_set[1]))