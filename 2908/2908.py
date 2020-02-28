import sys
input = sys.stdin.readline

a, b = input().split()
a = int("".join(a)[::-1])
b = int("".join(b)[::-1])
if a > b:
    print(a)
else:
    print(b)