def solution(n):
    ans = 0
    
    while n:
        if not n % 2:
            n //= 2
        else:
            n -= 1
            ans += 1
            
    return ans
