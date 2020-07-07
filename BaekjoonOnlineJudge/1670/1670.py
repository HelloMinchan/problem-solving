import sys
input = sys.stdin.readline

N = int(input())

memoization = [0] * (N + 1)
memoization[0] = memoization[2] = 1

for i in range(4, N + 1, 2):
    for j in range(0, i - 2 + 1, 2):
        memoization[i] += memoization[j] * memoization[i - j - 2]
        memoization[i] %= 987654321

print(memoization[N])
