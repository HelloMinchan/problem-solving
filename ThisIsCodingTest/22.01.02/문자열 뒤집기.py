import sys
input = sys.stdin.readline

S: str = input().rstrip()

# 정답 변수
answer: int = 0
# 이전 문자 기록 변수
before_character: str = ""
# 변환 기준 문자(마지막이거나, 처음이거나)
last_character: str = S[-1]

# 타겟은 현재 문자
for target in S:
    # 타겟이 마지막에 있는 문자와 같으면
    if target == last_character:
        # 이전 문자 기록
        before_character = target
        continue
    else:
        # 이전 문자와 타겟이 같으면
        if before_character == target:
            continue
        else:
            # 이전 문자 기록
            before_character = target
            # 정답 증가
            answer += 1
            
print(answer)