from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
students = list(sorted(map(int, input().split())))

student_dict = defaultdict(int)

for student in students:
    student_dict[student] += 1

answer = 0

for base_index in range(N - 2):
    left = base_index + 1
    right = N - 1

    while left < right:
        team = students[base_index] + students[left] + students[right]

        if team == 0:
            if students[left] == students[right]:
                answer += right - left
            else:
                answer += student_dict[students[right]]

            left += 1
        else:
            if team < 0:
                left += 1
            else:
                right -= 1

print(answer)
