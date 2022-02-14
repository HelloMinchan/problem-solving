# 3:37 ~ 3:40 (3분)
import sys

input = sys.stdin.readline

N = int(input())

for number in range(1, N + 1):
    constructor = number

    for digit in str(number):
        constructor += int(digit)

    if constructor == N:
        print(number)
        break
else:
    print(0)