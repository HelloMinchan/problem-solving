import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

left = 1
right = max(lans)

while left <= right:
    processdLans = 0
    mid = (right + left) // 2

    for lan in lans:
        processdLans += lan // mid

    if N <= processdLans:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(result)