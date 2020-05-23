import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
print(a * int(str(b)[2]))
print(a * int(str(b)[1]))
print(a * int(str(b)[0]))
print(a * b)