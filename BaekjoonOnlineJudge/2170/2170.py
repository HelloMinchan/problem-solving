import sys
input = sys.stdin.readline

N = int(input())

dots = [list(map(int, input().split())) for _ in range(N)]

dots.sort()

start = 0
end = 0
answer = 0

for s, e in dots:
    if not start:
        start = s
        end = e
        continue

    if end >= s:
        if end < e:
            end = e
    else:
        answer += end - start
        start = s
        end = e

answer += end - start

print(answer)
