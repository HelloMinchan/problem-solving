import sys
input = sys.stdin.readline

# input 값 저장
N, M, K = map(int, input().split())
numbers = list(reversed(sorted(map(int, input().split()))))

# 정답 변수
answer = 0
# 정답에 더할 인덱스의 현재 위치를 가르키는 포인터 변수
pointer = 0
# 현재 위치한 인덱스의 값을 몇번 더했는지 저장하는 카운터 변수
accumulated_count = 0

# M번 반복문을 돌림
for _ in range(M):
    # 정답에 현재 인덱스의 값을 더함
    answer += numbers[pointer]

    # 현재 인덱스 값을 한 번 더했음을 기록
    accumulated_count += 1

    # 만약 포인터가 0이 아니면, 포인터와 카운터 변수를 0으로 초기화 
    if pointer != 0:
        pointer = 0
        accumulated_count = 0
        continue
    
    # 카운터 변수가 K가 됐을 경우 포인터를 1 증가
    if accumulated_count == K:
        pointer += 1

print(answer)