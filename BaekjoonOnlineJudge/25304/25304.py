import sys

input = sys.stdin.readline

X = int(input())
N = int(input())

sum = 0

for _ in range(N):
    a, b = map(int, input().split())

    sum += a * b

if sum == X:
    print("Yes")
else:
    print("No")
