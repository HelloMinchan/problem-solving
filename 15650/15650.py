import sys
input = sys.stdin.readline


def DFS(index):
    global N, M, nums, visit, stack

    if len(stack) == M:
        print(*stack)
        return

    for i in range(index, N):
        if not visit[i]:
            visit[i] = True
            stack.append(nums[i])
            DFS(i)
            visit[i] = False
            stack.pop()


N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
visit = [False] * N
stack = []

DFS(0)