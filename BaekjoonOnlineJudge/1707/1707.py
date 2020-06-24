import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(sv, mark):
    visit[sv] = mark

    for i in adjList[sv]:
        if not visit[i]:
            if not DFS(i, -mark):
                return False
        else:
            if visit[i] == visit[sv]:
                return False
    return True


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    adjList = [[] for _ in range(V + 1)]
    visit = [False] * (V + 1)

    for _ in range(E):
        sv, dv = map(int, input().split())

        adjList[sv].append(dv)
        adjList[dv].append(sv)

    isBG = True
    for i in range(1, V + 1):
        if not visit[i]:
            if not DFS(i, 1):
                isBG = False
                break
    
    print("YES" if isBG else "NO")
