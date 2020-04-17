import sys
input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
memoization = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        memoization[1] = wines[1]
        continue
    elif i == 2:
        memoization[2] = wines[1] + wines[2]
        continue

    memoization[i] = max(memoization[i - 3] + wines[i - 1] + wines[i], memoization[i - 2] + wines[i], memoization[i - 1])

print(memoization[-1])