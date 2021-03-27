import sys

input = sys.stdin.readline

n = int(input())
boxes = [0] + list(map(int, input().split()))
memoization = [0]


for box in boxes:
    if memoization[-1] < box:
        memoization.append(box)
    else:
        left = 0
        right = len(memoization)

        while left < right:
            mid = (left + right) // 2

            if memoization[mid] < box:
                left = mid + 1
            else:
                right = mid

        memoization[right] = box

print(len(memoization) - 1)
