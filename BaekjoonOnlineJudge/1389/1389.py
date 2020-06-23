import sys
input = sys.stdin.readline


def floydWarshall():
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])


N, M = map(int, input().split())

INF = 2147483647
adjMatrix = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N):
    adjMatrix[i][i] = 0

for _ in range(M):
    sv, dv = map(int, input().split())

    adjMatrix[sv][dv] = adjMatrix[dv][sv] = 1

floydWarshall()

kevinB = []
for i in range(1, N + 1):
    temp = 0
    for j in range(1, N + 1):
        if i != j:
            temp += adjMatrix[i][j]
    kevinB.append((temp, i))

print(sorted(kevinB)[0][1])
