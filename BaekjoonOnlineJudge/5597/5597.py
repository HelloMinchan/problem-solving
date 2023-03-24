import sys

input = sys.stdin.readline

students = [int(input()) for _ in range(28)]

for number in range(1, 31):
    if number not in students:
        print(number)
