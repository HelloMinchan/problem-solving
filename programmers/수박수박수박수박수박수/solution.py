def solution(n):
    answer = ''
    
    for _ in range(n // 2):
        answer += "수박"
        
    if n % 2:
        return answer + "수"
    
    return answer