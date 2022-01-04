import sys
input = sys.stdin.readline

current_location = input().rstrip()

# 체스판의 최대 길이
CHESS_BOARD_LENGTH = 8
# 열의 문자를 숫자로 바꿔줄 사전
alphabet_to_number_dict = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7,
}

# 현재 행 위치
now_x = int(current_location[1]) - 1
# 현재 열 위치
now_y = alphabet_to_number_dict[current_location[0]]

# 방향 벡터
dx = [-2,-2,-1,1,2,2,-1,1]
dy = [-1,1,2,2,-1,1,-2,-2]

# 정답 변수
answer = 0

# 방향 벡터로 이동이 가능한지? 
for way in range(CHESS_BOARD_LENGTH):
    i = now_x + dx[way]
    j = now_y + dy[way]

    if i < 0 or i > CHESS_BOARD_LENGTH - 1 or j < 0 or j > CHESS_BOARD_LENGTH - 1:
        continue
    
    print(i, j)
    answer += 1

print(answer)

