from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip(); n = int(input()); nums = input().rstrip()

    if n:
        dq = deque(nums[1:-1].split(','))
    else:
        dq = deque()
    
    isReverse = False
    for order in p:
        if order == 'R':
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
            print('[', ",".join(reversed(list(dq))), ']', sep="")
        else:
            print('[', ",".join(list(dq)), ']', sep="")
