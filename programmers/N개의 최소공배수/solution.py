from collections import deque


def GCD(a, b):
    return b if not a % b else GCD(b, a % b)


def solution(arr):
    dq = deque(arr)
    
    while len(dq) != 1:
        num1 = dq.popleft()
        num2 = dq.popleft()
        
        dq.append(num1 * num2 // GCD(num1, num2))
        
    return dq[0]
