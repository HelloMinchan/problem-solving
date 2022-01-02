import sys
input = sys.stdin.readline

N = int(input())
fear_list = list(sorted(map(int, input().split())))

# 정답 변수
answer = 0
# 그룹의 인원 수
group_count = 0

# 인원의 공포도 가져옴
for fear in fear_list:
    # 인원 수 추가
    group_count += 1

    # 인원 수가 공포도와 같으면
    if group_count == fear:
        # 그룹이 만들어짐
        answer += 1
        # 인원 수 초기화
        group_count = 0

print(answer)