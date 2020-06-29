import sys
input = sys.stdin.readline

N = int(input())

triangle = [0, 1]
origin = 1
nextLine = 2
while 1:
    triangle.append(triangle[-1] + origin + nextLine)
    origin = origin + nextLine
    nextLine += 1
    if triangle[-1] + origin + nextLine > 300000:
        break

memoization = [2147483647] * (300001)
for i in range(len(triangle)):
    memoization[triangle[i]] = 1
    for j in range(triangle[i] + 1, N + 1):
        memoization[j] = min(memoization[j], memoization[j - triangle[i]] + 1)
        
print(memoization[N])
