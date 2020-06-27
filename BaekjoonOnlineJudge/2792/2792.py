import sys
input = sys.stdin.readline


def divide(mid):
    count = 0

    for j in jews:
        if not j % mid:
            count += j // mid
        else:
            count += j // mid + 1
    
    return count


N, M = map(int, input().split())
jews = [int(input()) for _ in range(M)]

left = 1
right = 1000000000

while left <= right:
    mid = (left + right) // 2

    if N >= divide(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
