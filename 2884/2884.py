import sys
input = sys.stdin.readline

h, m = map(int, input().split())

if m - 45 >= 0:
    print(h, m - 45)
else:
    if h == 0:
        print(23, 60 - (45 - m))
    else:
        print(h - 1, 60 - (45 - m))