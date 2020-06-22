from collections import deque


def solution(n, a, b):
    answer = 0
    dq = deque([x for x in range(1, n + 1)])
    
    while 1:
        dqsize = len(dq)
        answer += 1        
        for _ in range(0, dqsize, 2):
            compe1 = dq.popleft()
            compe2 = dq.popleft()

            if (compe1 == a and compe2 == b) or (compe1 == b and compe2 == a):
                return answer
            elif compe1 == a or compe1 == b:
                dq.append(compe1)
            elif compe2 == a or compe2 == b:
                dq.append(compe2)
            else:
                dq.append(compe1)
