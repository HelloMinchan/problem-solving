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

    if find_a > find_b:
        disjoint_set[find_b] = find_a
    elif find_a < find_b:
        disjoint_set[find_a] = find_b
    else:
        return


n, m = map(int, input().split())

disjoint_set = list(range(n+1))

for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")


