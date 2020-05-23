import sys
input = sys.stdin.readline

c = int(input())

for _ in range(c):
    n, m = map(int, input().split())
    sequenceA = list(map(int, input().split()))
    sequenceB = list(map(int, input().split()))
    sequenceJ = set(sequenceA + sequenceB)
    LIS = [0]
    length = 0

    for num in sequenceJ:
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
    
    print(LIS)
    print(length)