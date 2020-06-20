def solution(board):
    if len(board) == 1:
        return max(board[0])
    
    maxSquare = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not i or not j:
                continue
                
            if board[i][j]:
                board[i][j] = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                
                if maxSquare < board[i][j]:
                    maxSquare = board[i][j]
    
    return maxSquare ** 2
