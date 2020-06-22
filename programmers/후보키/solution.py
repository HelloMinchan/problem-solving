def DFS(L, visit, n):
    global candidate, candidates
    
    if candidate:
        candidates.append(candidate[:])
    
    for i in range(L, n):
        if not visit[i]:
            visit[i] = True
            candidate.append(i)
            DFS(i + 1, visit, n)
            visit[i] = False
            candidate.pop()

    
def deleteCandidates(col):
    global candidates
    temp = []
    
    for cand in candidates:
        isPossible = True
        if set(col).issubset(set(cand)):
            isPossible = False
        if isPossible:
            temp.append(cand)
    
    candidates = temp[:]
                
    
def solution(relation):
    global candidate, candidates
    answer = 0
    candidate = []
    candidates = []
    visit = [False] * len(relation[0])
    
    DFS(0, visit, len(relation[0]))
    
    candidates.sort(key=lambda x: len(x))
    
    while candidates:
        hash_key = dict()
        isPossible = True
        for i in range(len(relation)):
            temp = ""
            for j in candidates[0]:
                temp += relation[i][j]
    
            if not hash_key.get(temp, 0):
                hash_key[temp] = 1
            else:
                isPossible = False
                break
                
        if isPossible:
            deleteCandidates(candidates[0])
            answer += 1
        else:
            candidates.remove(candidates[0])
        
    return answer
