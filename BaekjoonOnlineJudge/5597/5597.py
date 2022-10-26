students = [False for _ in range(31)]

for _ in range(28):
    number = int(input())
    students[number] = True

for i, s in enumerate(students[1:]):
    if not s:
        print(i + 1)
