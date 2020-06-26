import sys, bisect
input = sys.stdin.readline

N, H = map(int, input().split())

top = []
bottom = []

for i in range(N):
    if i % 2:
        top.append(int(input()))
    else:
        bottom.append(int(input()))

top.sort()
bottom.sort()

ans = 2147483647
ansCount = 0
for i in range(1, H + 1):
    obstruction = 0

    obstruction = len(top) - bisect.bisect(top, H - i)
    obstruction += len(bottom) - bisect.bisect_left(bottom, i)

    if ans == obstruction:
        ansCount += 1
    elif ans > obstruction:
        ans = obstruction
        ansCount = 1
    
print(ans, ansCount)
