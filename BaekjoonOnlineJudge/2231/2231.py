import sys

input = sys.stdin.readline

N = int(input())

for number in range(1, N + 1):
    if N == number + sum(map(int, list(str(number)))):
        print(number)
        break
else:
    print(0)
