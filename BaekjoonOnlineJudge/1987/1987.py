import sys
input = sys.stdin.readline


def DFS(i, j):
    if i == R - 1 and j == C - 1:
        return 1
    
    count = 1

    for way in range(4):
        ii = i + dx[way]
        jj = j + dy[way]
        
        if ii < 0 or ii > R - 1 or jj < 0 or jj > C - 1:
            continue

        if not visit[ord(board[ii][jj]) - ord('A')]:
            visit[ord(board[ii][jj]) - ord('A')] = True
            count = max(count, DFS(ii, jj) + 1)
            visit[ord(board[ii][jj]) - ord('A')] = False
    
    return count


R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
visit = [False] * 26
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

visit[ord(board[0][0]) - ord('A')] = True

print(DFS(0, 0))
