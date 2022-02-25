# 4:13 ~
import sys

input = sys.stdin.readline


def dfs(loc, e, use_very_big_jump):
    if loc == N - 1:
        answer.append(e)
        return
    elif loc > N - 1:
        return

    if not use_very_big_jump:
        dfs(loc + 3, e + K, True)

    dfs(loc + 1, e + data[loc][0], use_very_big_jump)
    dfs(loc + 2, e + data[loc][1], use_very_big_jump)


N = int(input())
data = []

for i in range(N - 1):
    data.append(list(map(int, input().split())))

K = int(input())
visit = [False for _ in range(N - 1)]

answer = []

dfs(0, 0, False)

print(min(answer))