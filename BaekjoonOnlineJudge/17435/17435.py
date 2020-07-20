from math import log
import sys
input = sys.stdin.readline

MAX = 500001
MAX_V = int(log(500000, 2)) + 1

m = int(input())
cF = list(map(int, input().split()))
sparceTable = [[0 for _ in range(MAX_V + 1)] for _ in range(MAX)]

for i in range(1, m + 1):
    sparceTable[i][0] = cF[i - 1]

for j in range(1, MAX_V + 1):
    for i in range(1, m + 1):
        sparceTable[i][j] = sparceTable[sparceTable[i][j - 1]][j - 1]

Q = int(input())

for _ in range(Q):
    n, x = map(int, input().split())

    for j in range(MAX_V, -1, -1):
        if n >= (1 << j):
            n -= (1 << j)
            x = sparceTable[x][j]

    print(x)
