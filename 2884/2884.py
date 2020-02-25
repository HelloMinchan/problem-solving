import sys
input = sys.stdin.readline

t, m = map(int, input().split())

if m - 45 >= 0:
    print(t, m - 45)
else:
    if t == 0:
        print(23, 60 - (45 - m))
    else:
        print(t - 1, 60 - (45 - m))