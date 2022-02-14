# 3:44 ~ 3:53 (9분)
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0

for h in range(24):
    for m in range(60):
        for s in range(60):
            hour = "0" + str(h) if h < 10 else str(h)
            minute = "0" + str(m) if m < 10 else str(m)
            second = "0" + str(s) if s < 10 else str(s)

            if str(K) in hour + minute + second:
                answer += 1

            if h == N and m == 59 and s == 59:
                print(answer)
                sys.exit(0)