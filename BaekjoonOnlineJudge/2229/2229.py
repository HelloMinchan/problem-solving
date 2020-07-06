import sys
input = sys.stdin.readline


def DFS(start):
    if start >= N:
        return 0
    
    if memoization[start] != -1:
        return memoization[start]
    
    for i in range(start, N):
        memoization[start] = max(memoization[start], seg[start][i] + DFS(i + 1))

    return memoization[start]


N = int(input())
scores = list(map(int, input().split()))

seg = [[0] * 1001 for _ in range(1001)]

for i in range(N - 1):
    minScore = scores[i]
    maxScore = scores[i]
    for j in range(i + 1, N):
        minScore = min(minScore, scores[j])
        maxScore = max(maxScore, scores[j])
        seg[i][j] = maxScore - minScore

memoization = [-1] * 1001

print(DFS(0))
