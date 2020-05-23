import sys
input = sys.stdin.readline


def DFS():
    global N, M, arr, visit, stack

    if len(stack) == M:
        print(*stack)
        return
        
    for i in range(N):
        if not visit[i]:
            visit[i] = True
            stack.append(arr[i])
            DFS()
            stack.pop()
            visit[i] = False


N, M = map(int, input().split())
arr = [x for x in range(1, N + 1)]

visit = [False] * N
stack = []

DFS()