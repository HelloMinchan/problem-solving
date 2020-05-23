import sys
input = sys.stdin.readline

n, x = map(int, input().split())
num = list(input().rstrip().split(' '))

for i in num:
    if int(i) < x:
        print(i, end=' ')