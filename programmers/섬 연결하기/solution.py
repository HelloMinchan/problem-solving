def find(target):
    global disjoint_set

    if disjoint_set[target] == target:
        return target

    disjoint_set[target] = find(disjoint_set[target])
    return disjoint_set[target]


def union(a, b):
    global disjoint_set

    findA = find(a)
    findB = find(b)

    if findA == findB:
        return False

    elif findA < findB:
        disjoint_set[findB] = findA
    else:
        disjoint_set[findA] = findB

    return True


def solution(n, costs):
    global disjoint_set
    answer = 0

    disjoint_set = list(range(n))

    costs.sort(key=lambda el: el[2])

    for cost in costs:
        if union(cost[0], cost[1]):
            answer += cost[2]

            if len(set(disjoint_set)) == 1:
                break

    return answer