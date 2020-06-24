import sys
input = sys.stdin.readline


def DFS(A):
    tot = 0
    for num in map(int, str(A)):
        tot += num ** P
    
    if tot in stack:
        while stack[-1] != tot:
            stack.pop()
        stack.pop()

        return

    stack.append(tot)

    DFS(tot)


A, P = map(int, input().split())
stack = [A]

DFS(A)

print(len(stack))
