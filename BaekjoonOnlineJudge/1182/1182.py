import sys
input = sys.stdin.readline


def DFS(si):
    global answer

    if len(stack) > 0:
        if sum(stack) == S:
            answer += 1

    for i in range(si, N):
        if not visit[i]:
            visit[i] = True
            stack.append(seq[i])
            DFS(i + 1)
            visit[i] = False
            stack.pop()


N, S = map(int, input().split())
seq = list(map(int, input().split()))
visit = [False] * N
stack = []
answer = 0

DFS(0)

print(answer)
