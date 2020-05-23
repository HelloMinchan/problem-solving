import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N = int(input())
    sequence = list(map(int, input().split()))

    LIS = [0]
    length = 0

    for num in sequence:
        if num > LIS[-1]:
            LIS.append(num)
            length += 1
            continue

        left = 0
        right = length
        while(left < right):
            mid = (left + right) // 2

            if num < LIS[mid]:
                right = mid
            else:
                left = mid + 1
        
        LIS[right] = num
    
    print(length)