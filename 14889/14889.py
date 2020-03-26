import sys
input = sys.stdin.readline


def dfs(index, people, stack, visit):
    global team
    if len(stack) == len(people) // 2:
        team.append(stack[:])
    for i in range(index, len(people)):
        if not visit[i]:
            stack.append(people[i])
            visit[i] = True
            dfs(i, people, stack, visit)
            stack.pop()
            visit[i] = False


N = int(input())
people = [x for x in range(N)]
stack = []
visit = [False] * N
S = [list(map(int, input().split())) for x in range(N)]
team = []

dfs(0, people, stack, visit)

limit = len(team)
balance = []
for i in range(limit // 2):
    sum1 = 0
    sum2 = 0
    for j in range(len(team[i])):
        for k in range(j + 1, len(team[i])):
            sum1 += S[team[i][j]][team[i][k]] + S[team[i][k]][team[i][j]]
            sum2 += S[team[limit - i - 1][j]][team[limit - i - 1][k]] + S[team[limit - i - 1][k]][team[limit - i - 1][j]]
    balance.append(abs(sum1 - sum2))

print(min(balance))