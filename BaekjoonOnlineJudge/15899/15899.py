import sys
input = sys.stdin.readline

N, M, C = map(int, (input().split()))

color = [0] + [list(map(int, input().split()))]
adjList = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    sv, dv = map(int, input().split())

    adjList[sv].append(dv)

for _ in range(M):
    v, c = map(int, input().split())
    print(v, c)
