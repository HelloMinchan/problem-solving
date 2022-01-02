from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
fear_queue = deque(reversed(sorted(map(int, input().split()))))

answer = 0
group_count = 0

while fear_queue:
    fear = fear_queue.popleft()

    if group_count == 0:
        group_count = fear - 1
    else:
        group_count -= 1
    
    if group_count == 0:
        answer += 1

print(answer)