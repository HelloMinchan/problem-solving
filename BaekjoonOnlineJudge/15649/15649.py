import sys

input = sys.stdin.readline

def dfs():
    if len(stack) == M:
        print(*stack)

    for n in range(1, N+1):
        if not visit[n]:
            visit[n] = True
            stack.append(n)
            dfs()
            visit[n] = False
            stack.pop()

N, M = map(int, input().split())
visit = [False for _ in range(N+1)]

stack = []
dfs()