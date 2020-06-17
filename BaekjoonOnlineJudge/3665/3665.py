from collections import deque
import sys
input = sys.stdin.readline


def topologicalSort():
    global isImpossible, isAmbiguous

    for _ in range(n):
        if not dq:
            isImpossible = True
            return
        if len(dq) > 1:
            isAmbiguous = True
            return

        target = dq.popleft()
        sequence.append(target)

        for x in adjList[target]:
            indegree[x] -= 1

            if not indegree[x]:
                dq.append(x)


T = int(input())

for _ in range(T):
    n = int(input())

    isImpossible = False
    isAmbiguous = False
    sequence = []
    indegree = [0] * (n + 1)
    adjList = [[] for _ in range(n + 1)]

    lastYear = list(map(int, input().split()))
    
    for i in range(0, n):
        for j in range(i + 1, n):
            indegree[lastYear[j]] += 1
            adjList[lastYear[i]].append(lastYear[j])

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())

        isNotFound = True

        for x in adjList[a]:
            if x == b:
                isNotFound = False
                indegree[b] -= 1
                indegree[a] += 1
                adjList[a].remove(b)
                adjList[b].append(a)
        
        if isNotFound:
            indegree[a] -= 1
            indegree[b] += 1
            adjList[b].remove(a)
            adjList[a].append(b)

    dq = deque()    
    for i in range(1, n + 1):
        if not indegree[i]:
            dq.append(i)
    
    topologicalSort()
    
    if isImpossible:
        print("IMPOSSIBLE")
    elif isAmbiguous:
        print("?")
    else:
        print(*sequence)
