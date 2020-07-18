import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(target):
    global answer

    visit[target] = True
    cycle.append(target)
    nextTarget = sel[target]

    if visit[nextTarget]:
        if nextTarget in cycle:
            answer += cycle[cycle.index(nextTarget):]
        return
    else:
        DFS(nextTarget)


T = int(input())

for _ in range(T):
    n = int(input())
    sel = [0] + list(map(int, input().split()))
    visit = [False] * (n + 1)
    answer = []

    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            DFS(i)
                
    print(n - len(answer))
