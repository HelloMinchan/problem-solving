import sys
input = sys.stdin.readline

def DFS():
    global answer

    total = sum(stack)

    if total == n:
        answer += 1
        return
    elif total > n:
        return

    for number in numbers:
        stack.append(number)
        DFS()
        stack.pop()

T = int(input())

for _ in range(T):
    n = int(input())

    numbers = [1, 2, 3]
    stack = []
    answer = 0

    DFS()

    print(answer)