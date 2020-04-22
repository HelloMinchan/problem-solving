import sys
input = sys.stdin.readline

str1 = "0" + input().rstrip()
str2 = "0" + input().rstrip()

N = len(str2)
M = len(str1)
memoization = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not i or not j:
            continue

        if str1[j] == str2[i]:
            memoization[i][j] = memoization[i - 1][j - 1] + 1
        else:
            if memoization[i - 1][j] > memoization[i][j - 1]:
                memoization[i][j] = memoization[i - 1][j]
            else:
                memoization[i][j] = memoization[i][j - 1]

lcsLength = memoization[-1][-1]
stack = []

for i in range(N - 1, 0, -1):
    for j in range(1, M):
        if memoization[i][j] == lcsLength:
            if str1[j] == str2[i]:
                stack.append(str1[j])
                lcsLength -= 1
                break
           
print(memoization[-1][-1])
print(*(stack.pop() for _ in range(len(stack))), sep="")