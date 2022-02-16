# 4:42 ~ 4:57 (15분)

import sys

input = sys.stdin.readline

N = int(input())
tips = sorted([int(input()) for _ in range(N)], reverse=True)

answer = 0

for rank, tip in enumerate(tips):
    if tip - rank >= 0:
        answer += tip - rank
    else:
        break

print(answer)
