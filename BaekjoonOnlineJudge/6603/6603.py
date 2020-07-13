import sys
input = sys.stdin.readline


def DFS(si):
    if len(stack) == 6:
        print(*stack)

    for i in range(si, k):
        if not visit[i]:
            visit[i] = True
            stack.append(seq[i])
            DFS(i + 1)
            visit[i] = False
            stack.pop()


while 1:
    case = list(map(int, input().split()))

    if case[0]:
        k = case[0]; seq = case[1:]

        stack = []
        visit = [False] * k

        DFS(0)
        print()
    else:
        break
