def solution(participant, completion):
    answer = ''
    d1 = dict()
    d2 = dict()
    
    for p in participant:
        d1[p] = d1.get(p,0) + 1
    
    for c in completion:
        d2[c] = d2.get(c,0) + 1
    
    for k, v in d1.items():
        if d2.get(k,0) != v:
            answer = k
            
    return answer