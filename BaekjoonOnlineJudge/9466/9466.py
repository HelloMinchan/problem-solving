import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(target):
    global answer

    visit[target] = True
    cycle.append(target)
    nextTarget = select_person[target]

    if visit[nextTarget]:
        if nextTarget in cycle:
            answer += cycle[cycle.index(nextTarget) :]
        return
    else:
        dfs(nextTarget)


T = int(input())

for _ in range(T):
    n = int(input())

    select_person = [0] + list(map(int, input().split()))
    visit = [False for _ in range(n + 1)]
    answer = []

    for i in range(1, n + 1):
        if not visit[i]:
            cycle = []
            dfs(i)

    print(n - len(answer))
