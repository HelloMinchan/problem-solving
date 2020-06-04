import sys, heapq as hq
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N, a, b = map(int, input().split())
    minHq = []
    maxHq = []
    value = 1983
    sumValue = 0

    for i in range(N):
        if len(minHq) == len(maxHq):
            hq.heappush(maxHq, -value)
        else:
            hq.heappush(minHq, value)

        if not i:
            sumValue += -maxHq[0]
            value = (value * a + b) % 20090711
            continue

        if -maxHq[0] > minHq[0]:
            t1 = -hq.heappop(maxHq)
            t2 = -hq.heappop(minHq)
            hq.heappush(maxHq, t2)
            hq.heappush(minHq, t1)
        
        sumValue += -maxHq[0]
        value = (value * a + b) % 20090711
    
    print(sumValue % 20090711)