import sys
input = sys.stdin.readline

stairNum = int(input())
stairs = [int(input()) for _ in range(stairNum)]
memoization = [0] * stairNum

if stairNum == 1:
    print(stairs[0])
    sys.exit(0)
if stairNum == 2:
    print(stairs[0] + stairs[1])
    sys.exit(0)

for i in range(stairNum):
    if not i:
        memoization[0] = stairs[0]
    elif i == 1:
        memoization[1] = stairs[0] + stairs[1]
    elif i == 2:
        if stairs[0] + stairs[2] > stairs[1] + stairs[2]:
            memoization[2] = stairs[0] + stairs[2]
        else:
            memoization[2] = stairs[1] + stairs[2]
    else:
        if stairs[i] + stairs[i - 1] + memoization[i - 3] > stairs[i] + memoization[i - 2]:
            memoization[i] = stairs[i] + stairs[i - 1] + memoization[i - 3]
        else:
            memoization[i] = stairs[i] + memoization[i - 2]

print(memoization[-1])