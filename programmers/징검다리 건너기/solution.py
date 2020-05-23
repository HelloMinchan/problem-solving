def isPossible(stones, k, mid):
    disappearedStones = 0
    
    for s in stones:
        if s - mid <= 0:
            disappearedStones += 1
            if disappearedStones == k:
                return False
        else:
            disappearedStones = 0
            
    return True

    
def solution(stones, k):
    answer = 0
    
    left = 0
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        
        if isPossible(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer + 1