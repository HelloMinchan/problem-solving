def find(target):
    global connectTable
    
    if connectTable[target] == target:
        return target
    
    connectTable[target] = find(connectTable[target])
    return connectTable[target]

    
def union(sv, dv):
    global connectTable
    
    findSV = find(sv)
    findDV = find(dv)
    
    if findSV == findDV:
        return False
    
    if findSV < findDV:
        connectTable[findDV] = findSV
    else:
        connectTable[findSV] = findDV
    
    return True


def kruskal(roads):
    global answer
    
    for w, sv, dv in roads:
        if union(sv, dv):
            answer += w

    
def solution(n, costs):
    global answer, connectTable
    
    answer = 0
    connectTable = [x for x in range(n)]
    roads = []
    
    for cost in costs:
        roads.append((cost[2], cost[0], cost[1]))
        roads.append((cost[2], cost[1], cost[0]))
    
    roads.sort()
    
    kruskal(roads)
    
    return answer
