def GCD(a, b):
    return b if not a % b else GCD(b, a % b)

def solution(w,h):
    return w * h - (w+h-GCD(w,h))