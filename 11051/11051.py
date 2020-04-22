import sys
input = sys.stdin.readline

N, K = map(int, input().split())
memoization = [1] + [0] * (N)

for i in range(1, N + 1):
    memoization[i] = memoization[i - 1] * i

print(memoization[N] // (memoization[N - K] * memoization[K]) % 10007)