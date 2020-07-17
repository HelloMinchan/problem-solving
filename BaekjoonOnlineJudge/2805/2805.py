import sys
input = sys.stdin.readline


def doCut(mid):
    temp = 0

    for h in high:
        if h - mid > 0:
            temp += h - mid
    
    return temp


N, M = map(int, input().split())
high = list(map(int, input().split()))

left = 0
right = max(high)
answer = 0

while left <= right:
    mid = (left + right) // 2

    treeLength = doCut(mid)

    if treeLength >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
