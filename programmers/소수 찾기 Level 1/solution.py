def solution(n):
    isPrime = [False] + [False] + [True] * (n-1)
    count = 0
    
    for i in range(2, n+1):
        if isPrime[i]:
            count += 1
            
            for j in range(i*2, n+1, i):
                isPrime[j] = False
                
    return count