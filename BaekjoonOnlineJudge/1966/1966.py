from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    docu = list(map(int, input().split()))
    dq = deque()
    for i, d in enumerate(docu):
        dq.append((d, i))
    
    answer = 0
    while dq:
        d, i = dq.popleft()

        if not dq:
            answer += 1
            print(answer)
            break 

        if d >= max(list(dq))[0]:
            answer += 1
            if i == M:
                print(answer)
                break
        else:
            dq.append((d, i))
