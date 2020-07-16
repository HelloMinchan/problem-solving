import sys
input = sys.stdin.readline

N = int(input())
memoization = [2147483647] * 1000001
memoization[1] = 0
memoization[2] = 1
memoization[3] = 1

for i in range(4, N + 1):
    if not i % 3:
        memoization[i] = min(memoization[i], memoization[i // 3] + 1)
    if not i % 2:
        memoization[i] = min(memoization[i], memoization[i // 2] + 1)
    memoization[i] = min(memoization[i], memoization[i - 1] + 1)

print(memoization[N])
