def solution(s):
    answer = ''
    index = 0
    
    for target in s:
        if target != ' ':
            if index % 2:
                answer += target.lower()
            else:
                answer += target.upper()
                
            index += 1
            continue
        
        index = 0
        answer += target
        
    return answer