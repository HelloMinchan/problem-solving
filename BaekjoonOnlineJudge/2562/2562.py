import sys
input = sys.stdin.readline

# 최댓값을 저장할 변수
max_num = 0
# 최댓값의 인덱스를 저장할 변수
index = 0

# 9개의 숫자를 입력 받음
for i in range(1, 10):
    input_num = int(input())

    # 최댓값 보다 입력 받은 숫자가 크다면
    if max_num < input_num:
        # 최댓값을 갱신함
        max_num= input_num
        # 현재 인덱스를 저장함
        index = i

# 답 출력
print(max_num)
print(index)
