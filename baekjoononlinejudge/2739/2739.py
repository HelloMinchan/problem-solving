import sys
input = sys.stdin.readline

num = int(input())

for i in range(1, 10):
    print(num, '*', i, '=', num * i)