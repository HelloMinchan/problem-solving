import sys
input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
stack = []

for i in range(N):
    while(True):
        if not len(stack):
            print(0, end=" ")
            stack.append((i + 1, tower[i]))
            break
        if stack[-1][1] > tower[i]:
            print(stack[-1][0], end=" ")
            stack.append((i + 1, tower[i]))
            break
        stack.pop()