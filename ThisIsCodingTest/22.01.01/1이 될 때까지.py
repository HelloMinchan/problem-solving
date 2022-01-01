import sys
input = sys.stdin.readline

# input값 저장
N, K = map(int, input().split())

# 정답 변수
answer = 0

# N이 1일떄까지 연산 무한 반복
while 1:
    # N이 1이면 연산 종료
    if N == 1:
        break
    
    # 연산 부분
    # 두 번째 연산
    if N % K == 0:
        N //= K
    # 첫 번쨰 연산
    else:
        N -= 1
    
    # 연산 했으니 횟수 +1
    answer += 1

# 정답 출력
print(answer)