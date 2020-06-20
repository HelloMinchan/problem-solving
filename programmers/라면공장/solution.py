import heapq


def solution(stock, dates, supplies, k):
    answer = 0
    
    hq = []
    index = 0
    while stock < k:
        for i in range(index, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(hq, -supplies[i])
            index += 1
        
        stock += -heapq.heappop(hq)
        answer += 1
        
    return answer
