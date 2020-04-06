import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def DFS(index):
    global N, C, x, visit, stack, distances
    distance = 0

    if len(stack) == C:
        for i in range(C - 1):
            if distance < abs(stack[i] - stack[i - 1]):
                distance = abs(stack[i] - stack[i - 1])

        distances.append(distance)

    for i in range(index, N):
        if not visit[i]:
            visit[i] = True
            stack.append(x[i])
            DFS(i)
            visit[i] = False
            stack.pop()


N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
visit = [False] * N
stack = []
distances = []

DFS(0)

print(min(distances))