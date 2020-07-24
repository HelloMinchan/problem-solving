import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))

memoization = [0] * (N + 1)
maxNum = 0
for i in range(1, N + 1):    
    for j in range(i):
        if A[i] > A[j]:
            memoization[i] = max(memoization[i], memoization[j] + 1)
            maxNum = max(maxNum, memoization[i])

print(maxNum)
