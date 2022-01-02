from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
fear_queue = deque(sorted(map(int, input().split())))


# 정답 변수
answer = 0
# 그룹의 인원수
group_count = 0

while fear_queue:
    print(fear_queue)
    fear = fear_queue.popleft()
    print("이번 공포도 ===>", fear)
    if group_count == 0:
        group_count = fear - 1
    else:
        group_count -= 1
    print("그룹 카운트", group_count)
    if group_count == 0:
        answer += 1
    
    print("그룹 수",answer)

print(answer)