import sys
input = sys.stdin.readline

N = int(input())
memoization = [0] * (N + 1)

for i in range(2, N + 1):
    if not i % 3:
        memoization[i] = min(memoization[i // 3] + 1, memoization[i - 1] + 1)
    elif not i % 2:
        memoization[i] = min(memoization[i // 2] + 1, memoization[i - 1] + 1)
    else:
        memoization[i] = memoization[i - 1] + 1

print(memoization[-1])
