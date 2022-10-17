import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

hour = C // 60
min = C % 60

A += hour
B += min

if B >= 60:
    A += 1
    B -= 60

if A >= 24:
    A -= 24

print(A, B)
