import sys
input = sys.stdin.readline


def DFS():
    global answer

    value = sum(stack)
    if value >= n:
        if value == n:
            answer += 1
        return

    for num in seq:
        stack.append(num)
        DFS()
        stack.pop()


T = int(input())

for _ in range(T):
    n = int(input())
    seq = [1, 2, 3]
    stack = []
    answer = 0

    DFS()

    print(answer)
