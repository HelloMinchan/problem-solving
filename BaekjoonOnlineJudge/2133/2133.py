import sys
input = sys.stdin.readline

N = int(input())
memoization = [0] * (N + 1)

for i in range(2, N + 1, 2):
    if i == 2:
        memoization[i] = 3
        continue

    if not i % 2:
        memoization[i] = memoization[i - 2] * 3
        memoization[i] += 2

        for j in range(2, i - 4 + 1, 2):
            memoization[i] += memoization[j] * 2

print(memoization[-1])
