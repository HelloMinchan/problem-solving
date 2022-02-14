# 5:40 ~

import sys

input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)])
answer = 0

for i, rope in enumerate(ropes):
    answer = max(answer, rope * (N - i))

print(answer)
