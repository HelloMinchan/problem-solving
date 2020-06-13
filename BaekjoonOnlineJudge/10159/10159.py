import sys
input = sys.stdin.readline

def floydWarshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if adjMatrix[i][k] and adjMatrix[k][j]:
                    adjMatrix[i][j] = 1

N = int(input())
M = int(input())

adjMatrix = [[0] * N for _ in range(N)]
    
for _ in range(M):
    a,b = map(int,input().split())

    adjMatrix[a-1][b-1] = 1

floydWarshall()

for i in range(N):
    ans = 0

    for j in range(N):
        if i == j:
            continue
        
        if not adjMatrix[i][j] and not adjMatrix[j][i]:
            ans += 1

    print(ans)