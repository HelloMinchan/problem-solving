import sys
input = sys.stdin.readline


def floydWarshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                adjMatrix[i][j] = min(adjMatrix[i][j], adjMatrix[i][k] + adjMatrix[k][j])


n, m = map(int, input().split())

INF = 2147483647
adjMatrix = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    adjMatrix[i][i] = 0

for _ in range(m):
    sv, dv, di = map(int, input().split())

    if di:
        adjMatrix[sv][dv] = 0
        adjMatrix[dv][sv] = 0
    else:
        adjMatrix[sv][dv] = 0
        adjMatrix[dv][sv] = 1

floydWarshall()

k = int(input())
for _ in range(k):
    sv, dv = map(int, input().split())

    print(adjMatrix[sv][dv])
