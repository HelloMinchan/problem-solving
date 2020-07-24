import sys
input = sys.stdin.readline

A, B, V = map(int, input().split())

left = 0
right = 1000000000
answer = 0

while left <= right:
    mid = (left + right) // 2

    if (A * mid) - (B * (mid - 1)) >= V:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
