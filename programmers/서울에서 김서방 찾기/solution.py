def solution(seoul):
    answer = '김서방은 '
    
    for index, name in enumerate(seoul):
        if name == "Kim":
            answer += str(index)
            break
    
    return answer + "에 있다"