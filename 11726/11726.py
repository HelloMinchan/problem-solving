import sys
input = sys.stdin.readline

n = int(input())
memoization = [0] * n

for i in range(n):
    if i == 0:
        memoization[0] = 1
        continue
    if i == 1:
        memoization[1] = 2
        continue

    memoization[i] = memoization[i - 1] + memoization[i - 2]
    
print(memoization[-1] % 10007)