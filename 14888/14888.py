# PyPy3 통과 Python 3 시간 초과
import sys
input = sys.stdin.readline


def DFS():
    global N, nums, visit, opers, stack, maximum, minimum

    if len(stack) == N - 1:
        result = nums[0]
        for i in range(1, len(nums)):
            if stack[i - 1] == "+":
                result += nums[i]
            elif stack[i - 1] == "-":
                result -= nums[i]
            elif stack[i - 1] == "*":
                result *= nums[i]
            else:
                if result < 0:
                    result = -(abs(result) // nums[i])
                    continue
                result //= nums[i]
        
        if result > maximum:
            maximum = result
        if result < minimum:
            minimum = result
    
    for i in range(len(opers)):
        if not visit[i]:
            visit[i] = True
            stack.append(opers[i])
            DFS()
            visit[i] = False
            stack.pop()


N = int(input())
nums = list(map(int, input().split()))
operCount = list(map(int, input().split()))
visit = [False] * sum(operCount)
opers = []
stack = []
maximum = -1000000000
minimum = 1000000000

for index, value in enumerate(operCount):
    for _ in range(value):
        if index == 0:
            opers.append("+")
        elif index == 1:
            opers.append("-")
        elif index == 2:
            opers.append("*")
        else:
            opers.append("/")

DFS()

print(maximum)
print(minimum)