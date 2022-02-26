import sys

input = sys.stdin.readline


def dfs():
    global answer

    if sum(stack) >= n:
        if sum(stack) == n:
            answer += 1
        return

    for i in range(1, 4):
        stack.append(i)
        dfs()
        stack.pop()


T = int(input())

for _ in range(T):
    n = int(input())

    answer = 0
    stack = []
    dfs()

    print(answer)