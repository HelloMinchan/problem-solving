import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

winPer = (Y * 100) // X

if winPer >= 99:
    print(-1)
    sys.exit(0)

left = 0
right = 1000000000

while left <= right:
    mid = (left + right) // 2

    newWinPer = ((Y + mid) * 100) // (X + mid)

    if newWinPer != winPer:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
