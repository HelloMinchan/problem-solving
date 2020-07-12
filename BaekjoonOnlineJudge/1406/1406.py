from collections import deque
import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = deque()

N = int(input())

for _ in range(N):
    temp = list(input().rstrip())

    if temp[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif temp[0] == "D":
        if right:
            left.append(right.popleft())
    elif temp[0] == "B":
        if left:
            left.pop()
    else:
        left.append(temp[2])

print("".join(left) + "".join(right))
