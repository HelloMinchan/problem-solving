import sys
input = sys.stdin.readline

N = int(input())
scores = [0] + list(map(int, input().split()))

memoization = [0] * (N + 1)

for i in range(1, N + 1):
    maxNum = 0
    minNum = 2147483647

    for j in range(i, 0, -1):
        maxNum = max(maxNum, scores[j])
        minNum = min(minNum, scores[j])
        memoization[i] = max(memoization[i], maxNum - minNum + memoization[j - 1])

print(memoization[-1])
