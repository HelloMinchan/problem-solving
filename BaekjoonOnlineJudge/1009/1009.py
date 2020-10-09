import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    num = 1
    for _ in range(b):
        num *= a
        if num % 10 == 0:
            num = a
        else:
            num %= 10
    if num % 10 == 0:
        print(10)
    else:
        print(num % 10)
