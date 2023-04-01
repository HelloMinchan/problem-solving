import sys

input = sys.stdin.readline


def dfs():
    global answer

    if stack and int("".join(stack)) > N:
        return

    if stack:
        number = int("".join(stack))
        answer = max(answer, number)

    for index in range(K):
        stack.append(str(elements[index]))
        dfs()
        stack.pop()


N, K = map(int, input().split())

elements = list(sorted(map(int, input().split()), reverse=True))
stack = []

answer = 0

dfs()

print(answer)
