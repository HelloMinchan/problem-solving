# 7:04 ~
import sys

input = sys.stdin.readline

N = int(input())
mus = sorted(list(map(int, input().split())))

if len(mus) % 2 == 0:
    answer = 0
    for i in range(N // 2):
        answer = max(answer, mus[i] + mus[N - i - 1])
    print(answer)
else:
    answer = 0
    for i in range(N // 2):
        answer = max(answer, mus[i] + mus[N - i - 2])
    print(answer)