import sys
input = sys.stdin.readline


def DFS(a):
    if visit[a]:
        return False 

    visit[a] = True

    for b in adjList[a]:
        if B[b] == -1 or not visit[B[b]] and DFS(B[b]):
            A[a] = b
            B[b] = a
            return True
    
    return False


MAX = 200

N, M = map(int, input().split())

A = [-1] * 201
B = [-1] * 201
adjList = [[] for _ in range(MAX)]

for i in range(N):
    temp = list(map(int, input().split()))

    for j in range(1, len(temp)):
        adjList[i].append(temp[j] - 1)

match = 0

for i in range(N):
    visit = [False] * MAX
    if DFS(i):
        match += 1

print(match)
