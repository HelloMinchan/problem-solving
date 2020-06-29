import sys
input = sys.stdin.readline


def DFS(i):
    isCycle = False

    if visit[i] == 1:
        return True

    visit[i] = 1

    for v in adjList[i]:
        if visit[v] != 2:
            isCycle = DFS(v)
            if isCycle:
                break
    
    visit[i] = 2

    return isCycle


N = int(input())

adjList = [[] for _ in range(N + 1)]
visit = [False] * 101
for i in range(1, N):
    _ = input()
    connect = map(int, input().split())

    for v in connect:
        adjList[i].append(v)

if DFS(1):
    print("CYCLE")
else:
    print("NO CYCLE")
