import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

K = H = 0

for i in range(N):
    for j in range(M):
        if city[i][j] == 'K':
            K = (i, j)
        elif city[i][j] == 'H':
            H = (i, j)
