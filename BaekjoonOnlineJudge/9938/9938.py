import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def find(target):
    if drawer[target] == target:
        return target

    drawer[target] = find(drawer[target])
    return drawer[target]


def union(d1, d2):
    findD1 = find(d1)
    findD2 = find(d2)

    drawer[findD1] = findD2


N, L = map(int, input().split())

drawer = list(range(L + 1))
visit = [False] * (L + 1)

for i in range(N):
    d1, d2 = map(int, input().split())

    if not visit[d1]:
        visit[d1] = True
        union(d1, d2)
        print("LADICA")
    elif not visit[d2]:
        visit[d2] = True
        union(d2, d1)
        print("LADICA")
    elif not visit[find(d1)]:
        visit[find(d1)] = True
        union(d1, d2)
        print("LADICA")
    elif not visit[find(d2)]:
        visit[find(d2)] = True
        union(d2, d1)
        print("LADICA")
    else:
        print("SMECE")
