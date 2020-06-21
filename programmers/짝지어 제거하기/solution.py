def solution(s):
    stack = []
    
    for char in s:
        if not stack:
            stack.append(char)
            continue
        
        if stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    if stack:
        return 0
    return 1