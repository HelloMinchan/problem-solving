def solution(people, limit):
    answer = 0
    
    people.sort()
    
    left = 0
    right = len(people) - 1
    overLimit = 0
    
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            answer += 1
        else:
            overLimit += 1
            right -= 1
            
            if left == right:
                overLimit += 1
                break
            
    return answer + overLimit
