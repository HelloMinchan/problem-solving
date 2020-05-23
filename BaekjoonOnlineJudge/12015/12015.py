import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
LIS = [0]
length = 0

for num in A:
    if num > LIS[-1]:
        LIS.append(num)
        length += 1
    else:
        left = 0
        right = len(LIS)

        while right - left > 0:
            mid = (left + right) // 2

            if LIS[mid] < num:
                left = mid + 1
            else:
                right = mid

        LIS[right] = num

print(length)