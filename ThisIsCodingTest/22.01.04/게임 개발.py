import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, direction = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

# 북, 서, 남, 동 순
dx = [-1,0,1,0]
dy = [0,-1,0,1]
# 한장소에 얼마나 있었는지
count = 0
# 처음 있는 장소도 세야하니 1부터 시작
answer = 1
# 처음 있는 장소는 와봤음을 표시
matrix[x][y] = 1

while 1:
    # 왼쪽방향으로 회전
    direction = (direction + 1) % 4
    # 한장소에 한 번 있었음
    count += 1

    # 모든 방향을 다 보았을때
    if count == 5:
        # 한 장소에 있었던 횟수 초기화
        count = 0
        # 뒤로 빠꾸
        i = x - dx[direction]
        j = x - dy[direction]

        # 뒤로 갈 곳이 없으면 끝
        if i < 0 or i > N - 1 or j < 0 or j > M -1:
            break
        # 뒤로 갈 곳이 이미 갔던 곳이거나 바다면 끝
        if matrix[i][j] == 1:
            break
        
        # 뒤로 가서 동 서 남 북 확인
        for way in range(4):
            ii = i + dx[way]
            jj = j + dy[way]

            if ii < 0 or ii > N - 1 or jj < 0 or jj > M -1:
                continue
            
            # 갈 곳이 있으면 뒤로 간다
            if matrix[ii][jj] == 0:
                x = i
                y = j
                break
        else:
            break
    else:
        # 현재 바라보는 방향을 가봄    
        i = x + dx[direction]
        j = y + dy[direction]
        
        if i < 0 or i > N - 1 or j < 0 or j > M -1:
            continue
        
        # 안 가본 육지일 경우 간다.
        if matrix[i][j] == 0:
            matrix[i][j] = 1
            x = i
            y = j
            count = 0
            answer += 1
    
print(answer)