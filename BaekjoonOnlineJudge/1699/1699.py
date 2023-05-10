import sys

input = sys.stdin.readline

N = int(input())

memoization = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    memoization[i] = i

    for j in range(1, N + 1):
        if j**2 > i:
            break

        memoization[i] = min(memoization[i], memoization[i - j**2] + 1)

print(memoization[N])
