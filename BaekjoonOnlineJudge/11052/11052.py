import sys
input = sys.stdin.readline

N = int(input())
P = [0] + list(map(int, input().split()))
memoization = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i + 1):
        memoization[i][j] = P[j] + max(memoization[i - j])

print(max(memoization[-1]))
