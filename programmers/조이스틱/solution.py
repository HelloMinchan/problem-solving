def solution(name):
    answer = 0
    name = list(name)
    
    shouldChange = 0
    for n in name:
        if n != "A":
            shouldChange += 1
    
    if not shouldChange:
        return 0
    
    goLeft = 0
    goRight = 0
    index = 0
    
    while 1:
        if name[index] != "A":
            answer += min(ord('Z') - ord(name[index]) + 1, ord(name[index]) - ord("A"))
            
            name[index] = "A"
            shouldChange -= 1
        
        if not shouldChange:
            break
            
        goLeft = goRight = index
        move = 0

        while 1:
            goRight += 1
            goLeft -= 1
            move += 1

            if goLeft < 0:
                goLeft = len(name) - 1
            if goRight > len(name) - 1:
                goRight = 0

            if name[goRight] != "A":
                answer += move
                index = goRight
                break
            elif name[goLeft] != "A":
                answer += move
                index = goLeft
                break
            
    return answer
