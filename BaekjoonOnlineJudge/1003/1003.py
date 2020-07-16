import sys
input = sys.stdin.readline

memoization = [0] * 41
memoization[1] = 1

for i in range(2, 41):
    memoization[i] = memoization[i - 1] + memoization[i - 2]

T = int(input())

for _ in range(T):
    N = int(input())
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(memoization[N - 1], memoization[N])
