# 문자열 w를 u, v로 분리하는 함수
def divide(w):
    openP = 0
    closeP = 0
    
    for i in range(len(w)):
        if w[i] == '(':
            openP += 1
        else:
            closeP += 1
        if openP == closeP:
            return w[:i + 1], w[i + 1:]


# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def isBalanced(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
            
    return True


def solution(w):
    # 과정 1
    if not w:
        return ""
    
    # 과정 2
    u, v = divide(w)
    
    # 과정 3
    if isBalanced(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'
        
        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('
        
        # 과정 4-5
        return answer
