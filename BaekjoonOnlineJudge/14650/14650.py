import sys

input = sys.stdin.readline


def DFS(depth):
    global answer
    if depth == N:
        number = int("".join(map(str, stack)))
        if number % 3 == 0:
            if len(str(number)) == N:
                answer += 1
        return

    for index in range(len(numbers)):
        stack.append(numbers[index])
        DFS(depth + 1)
        stack.pop()


N = int(input())

if N == 1:
    print(0)
else:
    numbers = [0, 1, 2]
    stack = []
    answer = 0
    DFS(0)
    print(answer)