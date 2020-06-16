def solution(n):
    answer = ''
    form = ['4', '1', '2']
    
    while n:
        answer = form[n % 3] + answer
        
        if not n % 3:
            n = n // 3 - 1
        else:
            n //= 3
            
    return answer
