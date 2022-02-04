import sys

input = sys.stdin.readline

N = int(input())

for number in range(1, N + 1):
    number_constructor = number

    for digit_number in str(number):
        number_constructor += int(digit_number)

    if number_constructor == N:
        print(number)
        break
else:
    print(0)