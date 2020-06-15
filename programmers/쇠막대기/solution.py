def solution(arrangement):
    answer = 0
    
    stack = []
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            
            if arrangement[i - 1] == ')':
                answer += 1
            else:
                answer += len(stack)
                      
    return answer
