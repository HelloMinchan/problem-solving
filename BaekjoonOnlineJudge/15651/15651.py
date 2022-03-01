import sys

input = sys.stdin.readline

def dfs():
    if len(stack) == M:
        print(*stack)
        return

    for n in range(1, N+1):
        stack.append(n)
        dfs()
        stack.pop()


N, M = map(int, input().split())

stack = []
dfs()