import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
memoization = [0] * n
maxNum = -1001

for i in range(n):
    if not i:
        memoization[0] = maxNum = nums[0]
        continue

    if nums[i] < 0:
        if memoization[i - 1] > 0:
            if memoization[i - 1] + nums[i] > 0:
                memoization[i] = nums[i] + memoization[i - 1]
            else:
                memoization[i] = nums[i]
        else:
            memoization[i] = nums[i]
    else:
        if memoization[i - 1] > 0:
            memoization[i] = nums[i] + memoization[i - 1]
        else:
            memoization[i] = nums[i]
        
    if maxNum < memoization[i]:
        maxNum = memoization[i]

print(maxNum)