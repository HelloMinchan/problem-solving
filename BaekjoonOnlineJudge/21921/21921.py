from collections import deque, defaultdict
import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visited_counts = list(map(int, input().split()))

answer_dict = defaultdict(int)

window_sum = 0
window_queue = deque()

for visited_count in visited_counts:
    window_sum += visited_count
    window_queue.append(visited_count)

    if len(window_queue) == X:
        answer_dict[window_sum] += 1
        window_sum -= window_queue.popleft()


answer = list(sorted(answer_dict.items(), key=lambda answer: -answer[0]))

if answer[0][0] == 0:
    print("SAD")
else:
    print(answer[0][0])
    print(answer[0][1])
