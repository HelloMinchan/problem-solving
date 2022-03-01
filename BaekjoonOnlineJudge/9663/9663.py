import sys

input = sys.stdin.readline


def dfs(i):
    global answer

    if i == N:
        answer += 1
        return
    
    for j in range(N):
        if not row_visit[j] and not slash_visit[i+j] and not back_slash_visit[i-j]:
            row_visit[j] = slash_visit[i+j] = back_slash_visit[i-j] = True
            dfs(i+1)
            row_visit[j] = slash_visit[i+j] = back_slash_visit[i-j] = False


N = int(input())

slash_visit = [False for _ in range(((N - 1) * 2) + 1)]
back_slash_visit = [False for _ in range(((N - 1) * 2) + 1)]
row_visit = [False for _ in range(N)]

answer = 0

dfs(0)

print(answer)