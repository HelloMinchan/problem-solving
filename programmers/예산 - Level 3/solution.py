def solution(budgets, M):
    answer = 0
    
    left = 0
    right = max(budgets)
    
    while(left <= right):
        mid = (left + right) // 2
        
        isPossible = True
        dividend = 0
        for b in budgets:
            if b <= mid:
                dividend += b
            else:
                dividend += mid
                
        if dividend > M:
            isPossible = False
        
        if isPossible:
            answer = mid
            left = mid + 1
            continue
            
        right = mid -1
             
    return answer