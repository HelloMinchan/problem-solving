def solution(s, n):
    answer = ''
    
    for alpha in s:
        if alpha != ' ':
            asciiNum = ord(alpha) + n
            
            if alpha == 'z' or alpha == 'Z':
                asciiNum -= 26
            elif alpha.islower():
                if asciiNum >= 97 + 26:
                    asciiNum -= 26
            else:
                if asciiNum >= 65 + 26:
                    asciiNum -= 26
            
            answer += chr(asciiNum)
            continue
            
        answer += alpha
        
    return answer