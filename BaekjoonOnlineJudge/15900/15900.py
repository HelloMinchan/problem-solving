import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(sv, h):
    global answer
    
    if visit[sv]:
        return
    visit[sv] = True

    if len(adjList[sv]) == 1 and visit[adjList[sv][0]]:
        answer += h
        return

    for dv in adjList[sv]:
        if not visit[dv]:
            DFS(dv, h + 1)


N = int(input())
adjList = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
answer = 0

for _ in range(N - 1):
    sv, dv = map(int, input().split())

    adjList[sv].append(dv)
    adjList[dv].append(sv)

DFS(1, 0)

print("Yes" if answer % 2 else "No")
