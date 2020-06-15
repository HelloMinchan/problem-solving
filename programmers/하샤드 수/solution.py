def solution(x):
    if x % sum(map(int, str(x))):
        return False
    
    return True
