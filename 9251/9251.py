import sys
input = sys.stdin.readline

str1 = "0" + input().rstrip()
str2 = "0" + input().rstrip()

N = len(str1)
M = len(str2)
memoization = [[0] * M for _ in range(N)]

for i in range(len(str1)):
    for j in range(len(str2)):
        if not i or not j:
            continue

        if str1[i] == str2[j]:
            memoization[i][j] = memoization[i - 1][j - 1] + 1
        else:
            if memoization[i - 1][j] > memoization[i][j - 1]:
                memoization[i][j] = memoization[i - 1][j]
                continue
            memoization[i][j] = memoization[i][j - 1]

print(memoization[-1][-1])