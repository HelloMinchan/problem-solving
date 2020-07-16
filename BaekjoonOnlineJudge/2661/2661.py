import sys
input = sys.stdin.readline


def DFS(L):
    print(L, "===")
    for i in range(1, (L // 2) + 1):
        print(stack)
        print(stack[-i:], stack[-2 * i:-i])
        if stack[-i:] == stack[-2 * i:-i]:
            return -1
    
    if L == N:
        print(*stack, sep="")
        sys.exit(0)

    for j in range(1, 4):
        stack.append(str(j))
        DFS(L + 1)
        stack.pop()


N = int(input())

stack = []

DFS(0)
