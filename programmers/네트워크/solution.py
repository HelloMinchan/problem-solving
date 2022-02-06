def find(target):
    global disjoint_set

    if target == disjoint_set[target]:
        return target

    disjoint_set[target] = find(disjoint_set[target])
    return disjoint_set[target]


def union(a, b):
    global disjoint_set

    findA = find(a)
    findB = find(b)

    if findA == findB:
        return
    elif findA < findB:
        disjoint_set[findB] = findA
    else:
        disjoint_set[findA] = findB


def solution(n, computers):
    global disjoint_set
    disjoint_set = list(range(n))

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                union(i, j)

    for i in range(n):
        find(i)

    answer = len(set(disjoint_set))

    return answer