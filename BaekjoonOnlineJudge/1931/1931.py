import sys
input = sys.stdin.readline

N = int(input())
time = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))

end = time[0][1]
answer = 1

for t in time[1:]:
    if end <= t[0]:
        end = t[1]
        answer += 1

print(answer)
