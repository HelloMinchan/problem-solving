import sys
input = sys.stdin.readline


def floydWarshall():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                table[i][j] = min(table[i][j], table[i][k] + table[k][j])


n = int(input())

INF = 2147483647
table = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    table[i][i] = 0

while 1:
    sv, dv = map(int, input().split())

    if sv + dv == -2:
        break

    table[sv][dv] = 1
    table[dv][sv] = 1

floydWarshall()

score = []
for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if table[i][j] != INF:
            temp = max(temp, table[i][j])
    score.append((temp, i))
score.sort()

candidate = []
for s, i in score:
    if s > score[0][0]:
        break
    candidate.append(i)

print(score[0][0], len(candidate))
print(*candidate)
