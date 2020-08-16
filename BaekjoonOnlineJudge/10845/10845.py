from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
N = int(input())

for _ in range(N):
    order = input().split()

    # push
    if order[0] == "push":
        dq.append(int(order[1]))
    # pop
    elif order[0] == "pop":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    # size
    elif order[0] == "size":
        print(len(dq))
    # empty
    elif order[0] == "empty":
        if dq:
            print(0)
        else:
            print(1)
    # front
    elif order[0] == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    # back
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)
