def solution(board, moves):
    answer = 0
    stack = [0]
    
    for m in moves:
        isPush = False
        for j in range(len(board[0])):
            if board[j][m - 1] != 0:
                isPush = True
                stack.append(board[j][m - 1])
                board[j][m - 1] = 0
                break
        
        if isPush and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
        
    return answer