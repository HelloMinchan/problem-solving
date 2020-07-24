import sys
input = sys.stdin.readline


def install(mid):
    count = 1
    dist = coords[0] + mid

    for i in range(1, N):
        if coords[i] >= dist:
            dist = coords[i] + mid
            count += 1
    
    return count 


N, C = map(int, input().split())
coords = sorted([int(input()) for _ in range(N)])

left = 0
right = coords[-1]
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    count = install(mid)
    if count >= C:
        answer = mid
        left = mid + 1
    elif count < C:
        right = mid - 1
    
print(answer)
