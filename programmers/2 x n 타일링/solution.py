def solution(n):
    memoization = [0] * (n + 1)
    
    memoization[1] = 1
    memoization[2] = 2
    
    for i in range(3, n + 1):
        memoization[i] = (memoization[i - 1] + memoization[i - 2]) % 1000000007
        
    return memoization[n]
