import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def dfs(current_student_number):
    cycle_students.append(current_student_number)
    next_student_number = students[current_student_number]

    if not visit[next_student_number]:
        visit[next_student_number] = True
        dfs(next_student_number)
    else:
        if next_student_number in cycle_students:
            start_index = cycle_students.index(next_student_number)
            for student_number in cycle_students[start_index:]:
                is_match[student_number] = True


T = int(input())

for _ in range(T):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    is_match = [False for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]

    for student_number in range(1, n + 1):
        if not visit[student_number]:
            cycle_students = []

            dfs(student_number)

    print(is_match[1:].count(False))
