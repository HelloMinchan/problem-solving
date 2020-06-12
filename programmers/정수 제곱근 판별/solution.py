import math
def solution(n):
    if math.sqrt(n) % 1 == 0:
        return (math.sqrt(n)+1)**2
    
    return -1