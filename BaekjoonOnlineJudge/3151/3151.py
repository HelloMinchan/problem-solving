from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())

students = list(sorted(map(int, input().split())))
student_count = Counter(students)

answer = 0
for standard_index, student in enumerate(students):
    left = standard_index + 1
    right = N - 1

    while left < right:
        total = students[standard_index] + students[left] + students[right]

        if total == 0:
            if students[left] == students[right]:
                answer += right - left
            else:
                answer += student_count[students[right]]
            left += 1
        elif total > 0:
            right -= 1
        else:
            left += 1

print(answer)
