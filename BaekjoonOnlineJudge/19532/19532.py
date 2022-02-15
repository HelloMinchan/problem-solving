# 3:40 ~ 3:43 (3분)
import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            sys.exit(0)