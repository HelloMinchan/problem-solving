import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    time = 0
    remainingEatingTime = 0

    microwaveTime = list(map(int, input().split()))
    eatingTime = list(map(int, input().split()))
    total = []

    for i in range(N):
        time += microwaveTime[i]
        total.append((microwaveTime[i], eatingTime[i]))

    total = sorted(total, key=lambda x: (-x[1]))
    
    for i in range(0, N):
        remainingEatingTime -= total[i][0]
        remainingEatingTime = max(total[i][1], remainingEatingTime)
        
    time += remainingEatingTime

    print(time)