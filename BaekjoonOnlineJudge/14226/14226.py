from collections import deque
import sys
input = sys.stdin.readline


def BFS():
    dq = deque()
    dq.append((1, 0))
    
    while dq:
        before_monitor, before_clipBoard = dq.popleft()

        if before_monitor == S:
            print(memoization[before_monitor][before_clipBoard])
            sys.exit(0)

        for action in actions:
            if action == "copy":
                now_monitor = before_monitor
                now_clipBoard = now_monitor
            elif action == "paste":
                now_monitor = before_monitor + before_clipBoard
                now_clipBoard = before_clipBoard
            else:
                now_monitor = before_monitor - 1
                now_clipBoard = before_clipBoard

            if now_monitor < 0 or now_monitor > S:
                continue
            
            if not memoization[now_monitor][now_clipBoard]:
                dq.append((now_monitor, now_clipBoard))
                memoization[now_monitor][now_clipBoard] = memoization[before_monitor][before_clipBoard] + 1


S = int(input())
memoization = [[0]*(S+1) for _ in range(S+1)]
actions = ["copy", "paste", "delete"]

BFS()