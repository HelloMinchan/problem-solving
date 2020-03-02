import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
if b >= c :
    print(-1)
else:
    print(int(-a / (b - c)) + 1)