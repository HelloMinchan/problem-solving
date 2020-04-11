import sys
input = sys.stdin.readline

stairNum = int(input())
stairs = [int(input()) for _ in range(stairNum)]
memoization = [0]
count = 0

i = 0
while True:
    if i == stairNum - 1:
        break

    if i == stairNum - 2:
        if count == 0:
            memoization.append(memoization[-1] + stairs[i])
            memoization.append(memoization[-1] + stairs[i + 1])
            break
        else:
            memoization.append(memoization[-1] + stairs[i + 1])
            break
    
    if stairs[i] + memoization[-1] > stairs[i + 1] + memoization[-1]:
        if count != 2:
            memoization.append(stairs[i] + memoization[-1])
            count += 1
            i += 1
            continue

    memoization.append(stairs[i + 1] + memoization[-1])
    count = 0
    i += 2

print(memoization[-1])