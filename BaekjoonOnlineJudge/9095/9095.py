import sys

input = sys.stdin.readline


def dfs():
    global answer

    if sum(stack) >= n:
        if sum(stack) == n:
            answer += 1
        return
    
    for num in nums:
        stack.append(num)
        dfs()
        stack.pop()


T = int(input())
nums = [1,2,3]

for _ in range(T):
    n = int(input())
    
    answer = 0
    stack = []
    dfs()

    print(answer)
