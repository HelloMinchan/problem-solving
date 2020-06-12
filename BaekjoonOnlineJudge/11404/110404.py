import sys
input = sys.stdin.readline

def floydWarshall():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

n = int(input())
m = int(input())
INF = 2147483647
dist = [[0] * n] + [[0] + [INF] * n for _ in range(n)]

for i in range(1,n+1):
    dist[i][i] = 0

for _ in range(m):
    a,b,c = map(int,input().split())

    dist[a][b] = min(dist[a][b], c)

floydWarshall()

for i in range(1,n+1):
    for j in range(1,n+1):
        print(dist[i][j] if dist[i][j]!=INF else 0, end=" ")
    print()