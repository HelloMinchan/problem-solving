# 빠른 입출력
import sys
input = sys.stdin.readline

# 덱(파이썬에서는 일반 큐도 덱으로 사용)
from collections import deque

# N 입력 받음
N = int(input())

# 버려진 카드 모아놓을 리스트
deleted_card_list = []
# 1 부터 N까지 큐 초기화
queue = deque(list(range(1, N+1)))

while queue:
    # 1) 첫 번째 작업 : 재알 위에 있는 카드를 바닥에 버림
    deleted_card = queue.popleft()
    deleted_card_list.append(deleted_card)
    
    # 큐가 비었으면 반복문 종료
    if not queue:
        break

    # 2) 두 번째 작업 : 제일 위에 있는 카드 아래로 옮김
    top_card = queue.popleft()
    queue.append(top_card)

# 답 출력
print(*deleted_card_list)
