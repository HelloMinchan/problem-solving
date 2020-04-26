import sys, heapq
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    inputValue = int(input())
    
    if not inputValue:
        try:
            print(heapq.heappop(hq)[1])
        except:
            print(0)
    else:
        heapq.heappush(hq, (abs(inputValue), inputValue))