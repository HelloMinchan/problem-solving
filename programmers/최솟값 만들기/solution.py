import heapq


def solution(A, B):
    answer = 0
    minPQ = []
    maxPQ = []
    
    for i in range(len(A)):
        heapq.heappush(minPQ, A[i])
        heapq.heappush(maxPQ, -B[i])
        
    while minPQ:
        a = heapq.heappop(minPQ)
        b = -heapq.heappop(maxPQ)
        
        answer += a * b
        
    return answer
