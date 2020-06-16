def solution(s):
    if len(s) == 1:
        return 1
    
    answer = ""
    for c in range(1, len(s) // 2 + 1):
        start = 0
        finish = c
        
        temp = ""
        compString = ""
        compWord = dict()
        
        while 1:
            if start > len(s) - 1:
                break
                
            if not len(temp):
                temp = s[start:finish]
                compWord[temp] = 1
            else:
                if temp == s[start:finish]:
                    compWord[temp] = compWord[temp] + 1
                else:
                    compCount = compWord[temp]
                    if compCount > 1:
                        compString += str(compWord[temp])
                    compString += temp
                    
                    compWord = dict()
                    temp = s[start:finish]
                    compWord[temp] = 1
                    
            start += c
            finish += c
            
        compCount = compWord[temp]
        if compCount > 1:
            compString += str(compWord[temp])
        compString += temp
                    
        if not len(answer):
            answer = compString
        else:
            if len(answer) > len(compString):
                answer = compString
                
    return len(answer)
