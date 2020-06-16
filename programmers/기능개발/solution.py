from collections import deque


def solution(progresses, speeds):
    answer = []
    
    dq1 = deque(progresses)
    dq2 = deque(speeds)
    
    while(dq1):
        release = 0
        
        for i in range(len(dq2)):
            dq1[i] += dq2[i]
        
        while 1:
            if dq1 and dq1[0] >= 100:
                release += 1
                dq1.popleft()
                dq2.popleft()
            else:
                break
        
        if release:
            answer.append(release)
            
    return answer
