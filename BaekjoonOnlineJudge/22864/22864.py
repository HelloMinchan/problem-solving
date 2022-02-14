# 1:22 ~ 2:01
import sys

input = sys.stdin.readline

A, B, C, M = map(int, input().split())

if A > M:
    print(0)
else:
    answer = 0
    p = 0

    for _ in range(24):
        if p + A <= M:
            answer += B
            p += A
        else:
            p = 0 if p - C < 0 else p - C

    print(answer)