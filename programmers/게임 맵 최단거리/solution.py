from collections import deque


def BFS(maps, dx, dy, visit):
    dq = deque()
    visit[0][0] = True
    dq.append((0, 0))
    count = 1
    
    while dq:
        dqSize = len(dq)
        count += 1
        
        for _ in range(dqSize):
            i, j = dq.popleft()
            
            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]
                
                if ii < 0 or ii > len(maps) - 1 or jj < 0 or jj > len(maps[0]) - 1:
                    continue
                
                if ii == len(maps) - 1 and jj == len(maps[0]) - 1:
                    return count
                
                if not visit[ii][jj] and maps[ii][jj]:
                    visit[ii][jj] = True
                    dq.append((ii, jj))
                    
    return -1


def solution(maps):
    answer = 0
    
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    visit = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    return BFS(maps, dx, dy, visit)
