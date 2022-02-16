# 4:38 ~ 4:44 (6분)
import sys

input = sys.stdin.readline

N = int(input())
times = sorted(list(map(int, input().split())))

answer = 0
sum_stack = 0
for time in times:
    answer += time + sum_stack
    sum_stack += time

print(answer)
