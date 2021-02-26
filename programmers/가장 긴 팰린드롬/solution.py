def solution(string):
    answer = 0
    
    if len(string) == 1:
        return 1
    
    for i in range(len(string)-1):
        for j in range(1, len(string)+1):
            if string[i:j] == string[i:j][::-1]:
                answer = max(answer, len(string[i:j]))
        
    return answer