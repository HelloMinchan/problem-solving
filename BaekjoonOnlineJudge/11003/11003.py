from collections import deque
import sys

input = sys.stdin.readline

N, L = map(int, input().split())
INF = 2147482647

D = list(map(int, input().split()))

answer = []
window = deque()

for end, value in enumerate(D):
    # 덱에 들어있는 값이 현재 들어올 값보다 큰 경우 제외
    while window and window[-1][1] >= value:
        window.pop()

    # 덱에 들어있는 인덱스가 윈도우 크기를 벗어난 경우
    while window and window[0][0] < end - L + 1:
        window.popleft()

    window.append((end, value))

    answer.append(window[0][1])

print(*answer)