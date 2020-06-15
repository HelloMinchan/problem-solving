from collections import deque


def solution(priorities, location):
    answer = 0
    
    dq = deque()
    for i, p in enumerate(priorities):
        dq.append((i, p))
    
    priorities.sort(reverse=True)
    prioPointer = 0
    
    while 1:
        now = dq.popleft()
        
        if now[1] == priorities[prioPointer]:
            prioPointer += 1
            answer += 1
            if now[0] == location:
                break
        else:
            dq.append(now)
            
    return answer
