from collections import deque


def check(i, j, board, dx, dy, visit):
    isSame = True
    
    for way in range(3):
        ii = i + dx[way]
        jj = j + dy[way]
        
        if board[ii][jj] != board[i][j]:
            isSame = False
            break
    
    if isSame:
        if not visit[i][j]:
            visit[i][j] = True
            
        for way in range(3):
            ii = i + dx[way]
            jj = j + dy[way]
            
            if not visit[ii][jj]:
                visit[ii][jj] = True


def rebuild(m, n, board, visit):
    global answer
    
    isRebuild = False
    dq = deque()
    
    for i in range(n):
        for j in range(m):
            dq.append((board[i][j], visit[i][j]))
    
    for i in range(n):
        index = 0
        eraseCount = 0
        for j in range(m):
            block, isErase = dq.popleft()
            
            if not isErase:
                board[i][index] = block
                index += 1
            else:
                isRebuild = True
                answer += 1
                eraseCount += 1
                
        while eraseCount:
            board[i][index] = "NULL"
            index += 1
            eraseCount -= 1
    
    return isRebuild

    
def solution(m, n, board):
    global answer 
    
    answer = 0
    board = [list(reversed(x)) for x in zip(*board)]
    dx, dy = [0, 1, 1], [1, 0, 1]
    
    while 1:
        visit = [[False] * m for _ in range(n)]
        
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] != "NULL":
                    check(i, j, board, dx, dy, visit)
        
        if not rebuild(m, n, board, visit):
            break
        
    return answer
