def solution(weight):
    weight.sort()
    
    tot = 1
    for w in weight:
        if tot < w:
            break
        tot += w
    
    return tot
