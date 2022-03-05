import sys

input = sys.stdin.readline

def dfs(start):
    if len(stack) == M:
        print(*stack)
        return

    for number in range(start, N+1):
        stack.append(number)
        dfs(number)
        stack.pop()

N, M = map(int, input().split())

stack = []
dfs(1)