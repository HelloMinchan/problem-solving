# 3:27 ~ 3:36 (9분)
import sys

input = sys.stdin.readline


def dfs(index):
    global answer

    if len(stack) == 3:
        if sum(stack) <= M:
            answer = max(answer, sum(stack))
        return

    for i in range(index, N):
        if not visit[i]:
            visit[i] = True
            stack.append(cards[i])
            dfs(i + 1)
            visit[i] = False
            stack.pop()


N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
visit = [False for _ in range(N)]
stack = []

dfs(0)

print(answer)