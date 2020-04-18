import sys;
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
memoization = [1] * N
maxNum = 1

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            if memoization[j] + 1 > memoization[i]:
                memoization[i] = memoization[j] + 1
                if memoization[i] > maxNum:
                    maxNum = memoization[i]

print(maxNum)