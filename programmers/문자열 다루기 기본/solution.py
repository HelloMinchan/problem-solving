def solution(s):
    if s.isdecimal() and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False