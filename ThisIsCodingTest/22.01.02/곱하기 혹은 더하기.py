import sys
input = sys.stdin.readline

numbers = list(map(int, input().rstrip()))

answer = 0

for number in numbers:
    if answer == 0 or number in [0, 1]:
        answer += number
    else:
        answer *= number

print(answer)