import sys
input = sys.stdin.readline

N = int(input())

memoization = [[[0] * 401 for _ in range(401)] for _ in range(401)]
numberBox1 = [0] * 401
numberBox2 = [0] * 401
idx1 = 0
idx2 = 0

temp = list(map(int, input().split()))
for t in temp:
    if t:
        numberBox1[idx1] = t
        idx1 += 1

temp = list(map(int, input().split()))
for t in temp:
    if t:
        numberBox2[idx2] = t
        idx2 += 1

for k in range(1, N + 1):
    for i in range(1, min(idx1, k) + 1):
        for j in range(1, min(idx2, k) + 1):
            if i > k - 1 and j > k - 1:
                memoization[i][j][k] = memoization[i - 1][j - 1][k - 1] + numberBox1[i - 1] * numberBox2[j - 1]
            elif j > k - 1:
                memoization[i][j][k] = max(memoization[i][j - 1][k - 1], memoization[i - 1][j - 1][k - 1] + numberBox1[i - 1] * numberBox2[j - 1])
            elif i > k - 1:
                memoization[i][j][k] = max(memoization[i - 1][j][k - 1], memoization[i - 1][j - 1][k - 1] + numberBox1[i - 1] * numberBox2[j - 1])
            else:
                memoization[i][j][k] = max(memoization[i - 1][j][k - 1], memoization[i][j - 1][k - 1], memoization[i - 1][j - 1][k - 1] + numberBox1[i - 1] * numberBox2[j - 1])

print(memoization[idx1][idx2][N])
