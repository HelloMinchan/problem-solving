import heapq
def solution(s):
    low = []
    cap = []
    
    for alpha in s:
        if alpha.islower():
            heapq.heappush(low, -ord(alpha))
        else:
            heapq.heappush(cap, -ord(alpha))
    
    lowLength = len(low)
    capLength = len(cap)
    
    lowStr = "".join([chr(-heapq.heappop(low)) for _ in range(lowLength)])
    capStr = "".join([chr(-heapq.heappop(cap)) for _ in range(capLength)])
    
    return lowStr + capStr