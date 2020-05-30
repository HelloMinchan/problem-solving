from collections import deque
import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    K, N = map(int, input().split())
    dq = deque()
    prevSignal = 1983
    sumSignal = 0
    ans = 0

    for _ in range(N):
        nowSignal = prevSignal % 10000 + 1
        sumSignal += nowSignal
        dq.append(nowSignal)

        while sumSignal > K:
            sumSignal -= dq.popleft()
            
        if sumSignal == K:
            ans += 1
        
        prevSignal = (prevSignal * 214013 + 2531011) % (2 ** 32)
    
    print(ans)