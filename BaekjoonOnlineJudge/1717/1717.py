import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def find(target):
    if disjoint_set[target] == target:
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


n, m = map(int, input().split())

disjoint_set = list(range(n+1))

for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0:
        union(a, b)
    else:
        if find(b) == find(a):
            print("YES")
        else:
            print("NO")
