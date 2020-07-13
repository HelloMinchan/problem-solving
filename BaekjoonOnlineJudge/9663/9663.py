import sys
input = sys.stdin.readline


def DFS(L):
    global answer
    if L == N:
        answer += 1
        return

    for i in range(N):
        if not col[i] and not slash[i + L] and not backSlash[i - L + N - 1]:
            col[i] = slash[i + L] = backSlash[i - L + N - 1] = True
            DFS(L + 1)
            col[i] = slash[i + L] = backSlash[i - L + N - 1] = False


N = int(input())
col = [False] * N
slash = [False] * (2 * N - 1)
backSlash = [False] * (2 * N - 1)
answer = 0

DFS(0)

print(answer)
