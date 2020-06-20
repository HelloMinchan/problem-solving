def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        tot = i
        for j in range(i + 1, n + 1):
            tot += j
            if tot >= n:
                if tot == n:
                    answer += 1
                break
            
    return answer + 1
