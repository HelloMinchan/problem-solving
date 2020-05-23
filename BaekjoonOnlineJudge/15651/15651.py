import sys
input = sys.stdin.readline


def DFS():
    global N, M, nums, stack

    if len(stack) == M:
        print(*stack)
        return

    for i in range(N):    
        stack.append(nums[i])
        DFS()
        stack.pop()


N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
stack = []

DFS()