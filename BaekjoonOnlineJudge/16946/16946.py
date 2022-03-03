from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def bfs(dq, region_flag):
    region_area = 0
    while dq:
        i, j = dq.popleft()
        board[i][j] = region_flag
        region_area += 1

        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                continue

            if board[ii][jj] == "0" and not visit[ii][jj]:
                visit[ii][jj] = True        
                dq.append((ii, jj))
    
    return region_area


N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

region_flag = 0
region_area_dict = defaultdict(int)

for i in range(N):
    for j in range(M):
        if board[i][j] == "0" and not visit[i][j]:
            region_flag -= 1
            visit[i][j] = True

            dq = deque()
            dq.append((i,j))
            region_area = bfs(dq, region_flag)

            region_area_dict[region_flag] = region_area

zero_location = []
for i in range(N):
    for j in range(M):
        region_set = set()

        if board[i][j] == "1":
            for way in range(4):
                ii = i + dx[way]
                jj = j + dy[way]

                if ii < 0 or ii > N - 1 or jj < 0 or jj > M - 1:
                    continue

                if int(board[ii][jj]) < 0:
                    region_set.add(board[ii][jj])
            
            count = 1
            for region_flag in region_set:
                count += region_area_dict[region_flag]
            
            board[i][j] = str(count % 10)
        else:
            zero_location.append((i,j))

for i, j in zero_location:
    board[i][j] = "0"

for row in board:
    print("".join(row))