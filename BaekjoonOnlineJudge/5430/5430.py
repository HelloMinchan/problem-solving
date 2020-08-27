from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    nums = input().rstrip()

    if n == 0:
        if 'D' in p:
            print("error")
            continue

    dq = deque(nums[1:-1].split(','))

    isReverse = False

    for func in p:
        if func == 'R':
            isReverse = not isReverse
        else:
            if dq:
                if isReverse:
                    dq.pop()
                else:
                    dq.popleft()
            else:
                print("error")
                break
    else:
        if isReverse:
            print('[', ','.join(reversed(dq)), ']', sep="")
        else:
            print('[', ','.join(dq), ']', sep="")
