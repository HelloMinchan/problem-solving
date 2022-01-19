from re import S
import sys
input = sys.stdin.readline

LOTTO_NUMBER_COUNT = 6

def DFS():
    if len(stack) >= 2:
        if stack[-1] < stack[-2]:
            return

    if len(stack) == LOTTO_NUMBER_COUNT:
        print(*stack)
        return

    for index, number in enumerate(numbers[:]):
        if not visit[index]:
            visit[index] = True
            stack.append(number)
            DFS()
            visit[index] = False
            stack.pop()


while 1:
    numbers = list(map(int, input().split()))

    if numbers[0] == 0:
        break
    
    k = numbers[0]
    numbers = numbers[1:]
    visit = [False for _ in range(k)]
    stack = []

    DFS()
    print()