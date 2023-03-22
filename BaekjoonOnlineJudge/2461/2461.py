from collections import deque
import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())

student_queues = [deque(sorted(map(int, input().split()))) for _ in range(N)]

represent_student_hq = []
max_student = 0
for index, student_queue in enumerate(student_queues):
    student = student_queue.popleft()

    max_student = max(max_student, student)
    heapq.heappush(represent_student_hq, (student, index))

answer = sys.maxsize

while represent_student_hq:
    min_student, index = heapq.heappop(represent_student_hq)
    answer = min(answer, max_student - min_student)

    if student_queues[index]:
        new_represent_student = student_queues[index].popleft()
        max_student = max(max_student, new_represent_student)
        heapq.heappush(represent_student_hq, (new_represent_student, index))
    else:
        break

print(answer)
