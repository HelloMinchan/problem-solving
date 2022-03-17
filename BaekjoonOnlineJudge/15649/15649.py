import sys

input = sys.stdin.readline

def dfs():
    if len(stack) == M:
        print(*stack)
        return
        
    for number in range(1, N+1):
        if not visit[number]:
            visit[number] = True
            stack.append(number)
            dfs()
            visit[number] = False
            stack.pop()


N, M = map(int, input().split())

visit = [False for _ in range(N+1)]

stack = []
dfs()