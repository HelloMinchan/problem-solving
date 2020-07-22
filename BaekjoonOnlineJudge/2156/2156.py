import sys
input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(wines[1])
    sys.exit(0)

memoization = [0] * (n + 1)
memoization[1] = wines[1]
memoization[2] = wines[2] + wines[1]

for i in range(3, n + 1):
    memoization[i] = max(wines[i] + memoization[i - 2], wines[i] + wines[i - 1] + memoization[i - 3], memoization[i - 1])

print(memoization[-1])

