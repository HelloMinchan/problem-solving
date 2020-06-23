def DFS(begin, target, words, visit):
    global answer, stack
    
    if stack and stack[-1] == target:
        if answer > len(stack):
            answer = len(stack)
        return
    
    for i in range(len(words)):
        isDiff = 0
        
        if not visit[i]:
            if not stack:
                for j in range(len(begin)):
                    if begin[j] != words[i][j]:
                        isDiff += 1
            else:
                for j in range(len(stack[-1])):
                    if stack[-1][j] != words[i][j]:
                        isDiff += 1
                        
            if isDiff > 1:
                continue
                
            visit[i] = True
            stack.append(words[i])
            DFS(begin, target, words, visit)
            visit[i] = False
            stack.pop()
            
            
def solution(begin, target, words):
    if target not in words:
        return 0
    
    global answer, stack
    
    answer = 2147483647
    stack = []
    visit = [False] * len(words)
    
    DFS(begin, target, words, visit)
    
    return answer
