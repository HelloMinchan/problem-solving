import sys

input = sys.stdin.readline

def dfs(start):
    if len(stack) == M:
        print(*stack)
        return

    for n in range(start, N+1):
        stack.append(n)
        dfs(n+1)
        stack.pop()

N, M = map(int, input().split())

visit = [False for _ in range(N+1)]

stack = []
dfs(1)