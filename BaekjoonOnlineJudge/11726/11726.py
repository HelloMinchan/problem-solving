import sys
input = sys.stdin.readline

n = int(input())
memoization = [0] * 1001
memoization[1] = 1
memoization[2] = 2

for i in range(3, n + 1):
    memoization[i] = memoization[i - 1] + memoization[i - 2]
    memoization[i] %= 10007

print(memoization[n] % 10007)
