from collections import defaultdict


def find(target):
    global disjoint_set

    if disjoint_set[target] == target:
        return disjoint_set[target]

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


def solution(n, wires):
    global disjoint_set

    answer = 2147483647

    for i in range(len(wires)):
        disjoint_set = list(range(n + 1))

        for j in range(len(wires)):
            if i == j:
                continue
            else:
                union(wires[j][0], wires[j][1])

        for i in range(1, n + 1):
            find(i)

        if len(set(disjoint_set[1:])) != 2:
            continue

        com_dict = defaultdict(int)

        for count in disjoint_set[1:]:
            if count != 0:
                com_dict[count] += 1

        divide = com_dict.values()

        answer = min(answer, max(divide) - min(divide))

    return answer