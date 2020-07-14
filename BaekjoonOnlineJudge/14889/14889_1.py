import sys
input = sys.stdin.readline


def DFS(si):
    if len(divide) == N // 2:
        teamA.append(list(divide))
        teamB.append(list(total - divide))

    for i in range(si, N):
        if not visit[i]:
            visit[i] = True
            divide.add(i)
            DFS(i + 1)
            visit[i] = False
            divide.remove(i)
            

N = int(input())
visit = [False] * N

total = set(range(N))
divide = set()
teamA = []
teamB = []

adjMatrix = [list(map(int, input().split())) for _ in range(N)]

DFS(0)

answer = 2147483647

for i in range(len(teamA) // 2):    
    totA = 0
    totB = 0

    for j in range(len(teamA[i]) - 1):
        for k in range(j + 1, len(teamA[i])):
            totA += adjMatrix[teamA[i][j]][teamA[i][k]] + adjMatrix[teamA[i][k]][teamA[i][j]]
    
    for j in range(len(teamB[i]) - 1):
        for k in range(j + 1, len(teamB[i])):
            totB += adjMatrix[teamB[i][j]][teamB[i][k]] + adjMatrix[teamB[i][k]][teamB[i][j]]

    answer = min(answer, abs(totA - totB))

print(answer)
