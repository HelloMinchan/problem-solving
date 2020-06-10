def solution(heights):
    answer = [0] * len(heights)
    save  = []
    
    for i in range(len(heights) - 1,-1,-1):
        if not save:
            save.append((heights[i], i))
            continue
        
        while save and save[-1][0] < heights[i]:
            answer[save[-1][1]] = i + 1
            save.pop()
        
        save.append((heights[i], i))
        
    return answer