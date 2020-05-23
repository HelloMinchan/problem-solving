# 중복 조합
import sys
input = sys.stdin.readline


def DFS(index):
    global N, M, nums, stack
    if len(stack) == M:
        print(*stack)
        return
    for i in range(index, N):
        stack.append(nums[i])
        DFS(i)
        stack.pop()


N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
stack = []
DFS(0)

# 비내림차순 중복 순열
# import sys
# input = sys.stdin.readline

# def DFS(backNum):
#     global N, M, nums, stack

#     if len(stack) == M:
#         print(*stack)
#         return

#     for i in range(N):
#         if len(stack) and stack[-1] > nums[i]:
#             continue
#         stack.append(nums[i])
#         DFS(nums[i])
#         stack.pop()

# N, M = map(int, input().split())
# nums = [i for i in range(1, N + 1)]
# stack = []

# DFS(0)