def solution(n):
    count = format(n, 'b').count('1')
    
    i = n + 1
    while 1:
        if count == format(i, 'b').count('1'):
            return i
        i += 1
