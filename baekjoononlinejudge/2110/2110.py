import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = sorted([int(input()) for _ in range(N)])
result = 0
left = 0
right = max(x)

while left <= right:
    jump = mid = (left + right) // 2

    if mid * C > max(x):
        right = mid - 1
        continue
    
    count = 1
    interval = x[0] + jump
    for i in range(1, len(x)):
        if interval > x[i]:
            continue
        else:
            interval = x[i] + jump
            count += 1
    
    if count < C:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
        
print(result)