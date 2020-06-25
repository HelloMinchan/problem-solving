import sys
input = sys.stdin.readline


def travel(path):
    cost = 0

    for i in range(N - 1):
        if adjMatrix[path[i]][path[i + 1]]:
            cost += adjMatrix[path[i]][path[i + 1]]
        else:
            return -1
    
    if adjMatrix[path[N - 1]][path[0]]:
        cost += adjMatrix[path[N - 1]][path[0]]
    else:
        return -1
    
    return cost


def DFS():
    global minimumCost

    if len(stack) == N:
        cost = travel(stack)
        if cost != -1:
            minimumCost = min(minimumCost, cost)

    for i in range(N):
        if not visit[i]:
            visit[i] = True
            stack.append(i)
            DFS()
            visit[i] = False
            stack.pop()


N = int(input())
adjMatrix = [list(map(int, input().split())) for _ in range(N)]

minimumCost = 2147483647
stack = []
paths = []
visit = [False] * N

DFS()

print(minimumCost)
