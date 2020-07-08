import sys
input = sys.stdin.readline


def DFS(i, j):
    global memoization

    if i == N and j == M:
        return 1
    
    if memoization[i][j][0] != -1:
        return memoization[i][j][0]

    memoization[i][j][0] = 0
    
    for way in range(2):
        ii = i + dx[way]
        jj = j + dy[way]

        if ii < 0 or ii > N or jj < 0 or jj > M:
            continue

        if (ii, jj) not in memoization[i][j]:
            memoization[i][j][0] += DFS(ii, jj)
    
    return memoization[i][j][0]


N, M = map(int, input().split())
K = int(input())
dx, dy = [0, 1], [1, 0]
memoization = [[[-1] for _ in range(M + 1)] for _ in range(N + 1)]

for _ in range(K):
    temp = list(map(int, input().split()))
    memoization[temp[0]][temp[1]].append((temp[2], temp[3]))
    memoization[temp[2]][temp[3]].append((temp[0], temp[1]))

print(DFS(0, 0))
