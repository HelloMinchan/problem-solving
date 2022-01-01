import sys
input = sys.stdin.readline

# input값 저장
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 정답 변수
answer = 0

# 행렬에서 행들을 뽑아냄
for row in matrix:
    # 행의 최솟값이 정답 변수에 기록된 것보다 클 경우
    if answer < min(row):
        # 정답 변수에 기록
        answer = min(row)

print(answer)