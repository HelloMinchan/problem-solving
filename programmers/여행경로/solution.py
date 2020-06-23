from collections import defaultdict


def DFS(sv, sequence, stopover, n):
    global answer
    
    sequence.append(sv)
    
    for i in range(len(stopover[sv])):
        if stopover[sv][i] != "visit":
            dv = stopover[sv][i]
            
            stopover[sv][i] = "visit"
            temp = DFS(dv, sequence, stopover, n)
            
            if len(temp) == n + 1:
                answer.append(sequence[:])
                
            sequence.pop()
            stopover[sv][i] = dv

    return sequence


def solution(tickets):
    global answer
    
    answer = []
    
    stopover = defaultdict(list)
    
    for sv, dv in tickets:
        stopover[sv] = stopover.get(sv, []) + [dv]
    
    DFS("ICN", [], stopover, len(tickets))
    
    return sorted(answer)[0]
