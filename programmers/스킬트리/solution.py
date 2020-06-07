def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        seq = 0
        
        for s in st:
            if s in skill:
                if s != skill[seq]:
                    break
                else:
                    seq += 1
        else:
            answer += 1
        
    return answer