import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def check_ban(icecream, stack):
    for icecream_in_stack in stack:
        if ban_matrix[icecream][icecream_in_stack]:
            return False

    return True


def dfs(start):
    global answer, visit

    if len(stack) == 3:
        answer += 1
        return

    for icecream in range(start, N + 1):
        if not visit[icecream] and check_ban(icecream, stack):
            if stack and stack[-1] > icecream:
                continue

            visit[icecream] = True
            stack.append(icecream)
            dfs(start + 1)
            visit[icecream] = False
            stack.pop()


N, M = map(int, input().split())

ban_matrix = [[False for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    icecream1, icecream2 = map(int, input().split())
    ban_matrix[icecream1][icecream2] = True
    ban_matrix[icecream2][icecream1] = True

visit = [False for _ in range(N + 1)]
stack = []
answer = 0

dfs(1)

print(answer)
