from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def CtoI(target):
    if target.isupper():
        return ord(target) - ord('A')
    else:
        return ord(target) - ord('a') + 26


def BFS(source, sink, visit):
    dq = deque()
    dq.append(source)
    
    while dq and visit[sink] == -1:
        sv = dq.popleft()

        for dv in adjList[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visit[dv] == -1:
                dq.append(dv)
                visit[dv] = sv

                if dv == sink:
                    break
        
    if visit[sink] == -1:
        return True
    else:
        return False


def edmondsKarp(source, sink):
    totalFlow = 0

    while 1:
        visit = [-1] * MAX_V
        if BFS(source, sink, visit):
            break

        minFlow = INF
        
        i = sink
        while i != source:
            minFlow = min(minFlow, capacity[visit[i]][i] - flow[visit[i]][i])
            i = visit[i]
        
        i = sink
        while i != source:
            flow[visit[i]][i] += minFlow
            flow[i][visit[i]] -= minFlow
            i = visit[i]
        
        totalFlow += minFlow
    
    return totalFlow


MAX_V = 52
INF = 2147483647

N = int(input())
capacity = [[0] * MAX_V for _ in range(MAX_V)]
flow = [[0] * MAX_V for _ in range(MAX_V)]
adjList = [[] for _ in range(MAX_V)]

for _ in range(N):
    sv, dv, c = input().rstrip().split()

    sv = CtoI(sv)
    dv = CtoI(dv)

    capacity[sv][dv] += int(c)
    capacity[dv][sv] += int(c)
    adjList[sv].append(dv)
    adjList[dv].append(sv)

source = CtoI("A")
sink = CtoI("Z")

print(edmondsKarp(source, sink))
