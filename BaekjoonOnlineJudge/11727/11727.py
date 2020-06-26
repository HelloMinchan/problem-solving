import sys
input = sys.stdin.readline

n = int(input())

memoization = [0] * (n + 1)

for i in range(n + 1):
    if i == 1:
        memoization[i] = 1
        continue
    if i == 2:
        memoization[i] = 3
        continue

    memoization[i] = (memoization[i - 1] + (memoization[i - 2] * 2)) % 10007

print(memoization[-1])
