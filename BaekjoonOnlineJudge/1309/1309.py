import sys
input = sys.stdin.readline

N = int(input())

memoization = [0] * (N + 1)
memoization[0] = 1
memoization[1] = 3

for i in range(2, N + 1):
    memoization[i] = (memoization[i - 1] * 2 + memoization[i - 2]) % 9901

print(memoization[-1])
