import sys
input = sys.stdin.readline


def DFS():
    global M, li, visit, alreadyPrint, stack

    if len(stack) == M:
        alreadyPrint.append(tuple(stack[:]))
        return

    for i in range(len(li)):
        if not visit[i]:
            stack.append(li[i])
            visit[i] = True
            DFS()
            stack.pop()
            visit[i] = False


N, M = map(int, input().split())
li = (list(map(int, input().split())))

visit = [False] * len(li)
alreadyPrint = []
stack = []

DFS()

for x in sorted(list(set(alreadyPrint))):
    print(*x)