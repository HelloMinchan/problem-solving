from collections import deque


def solution(s):
    answer = []
    sLength = len(s)
    dq = deque()
    
    for i in range(sLength):
        tempNum = ""

        if s[i] != "{" and s[i] != "}":
            dq.append(s[i])

        if s[i] == "}":
            isPop = False

            while(len(dq)):
                isPop = True
                value = dq.popleft()
                
                if value != ",":
                    tempNum += value
                else:
                    if tempNum != "":
                        answer.append(tempNum)
                        tempNum = ""

            if isPop and tempNum != "":
                answer.append(tempNum)

    hash = []
    for i in range(100001):
        hash.append([i, 0])
    
    for num in list(map(int, answer)):
        hash[num][1] += 1
        
    temp = sorted(hash, reverse=True, key=lambda x : x[1])
    
    answer = []
    for num in temp:
        if num[1] == 0:
            break
        answer.append(num[0])
        
    return answer