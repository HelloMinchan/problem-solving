def find(target):
    global table
    
    if table[target] == target:
        return target
    
    table[target] = find(table[target])
    return table[target]


def union(a, b):
    global table
    
    findA = find(a)
    findB = find(b)
    
    if findA == findB:
        return
    if findA < findB:
        table[findB] = findA
    else:
        table[findA] = findB

        
def solution(n, computers):
    global table
    
    table = [x for x in range(n)]
    
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)
    
    for i in range(n):
        find(i)
        
    return len(set(table))
