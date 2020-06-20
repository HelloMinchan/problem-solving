def DFS(visit):
    global ans, stack
    
    if len(stack) == 3:
        ans.append(list(map(str, stack))[:])
        return
    
    for i in range(1, 10):
        if not visit[i]:
            visit[i] = True
            stack.append(i)
            DFS(visit)
            visit[i] = False
            stack.pop()


def checkPossible(num, strike, ball):
    global ans
    
    survival = []
    for ansNum in ans:
        strikeCount = 0
        ballCount = 0
        
        for i in range(3):
            if ansNum[i] == num[i]:
                strikeCount += 1
            else:
                if num[i] in ansNum:
                    ballCount += 1
                    
        if strikeCount == strike and ballCount == ball:
            survival.append(ansNum[:])
    
    ans = survival[:]        

            
def solution(baseball):
    global ans, stack
    
    ans = []
    
    stack = []
    visit = [False] * 10
    DFS(visit)
    
    for num, strike, ball in baseball:
        checkPossible(list(str(num)), strike, ball)
    
    return len(ans)
