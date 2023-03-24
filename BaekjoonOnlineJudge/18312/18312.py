import sys

input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
for hour in range(0, N + 1):
    if hour < 10:
        hour = "0" + str(hour)
    else:
        hour = str(hour)
    for minute in range(0, 60):
        if minute < 10:
            minute = "0" + str(minute)
        else:
            minute = str(minute)
        for second in range(0, 60):
            if second < 10:
                second = "0" + str(second)
            else:
                second = str(second)

            time_string = hour + minute + second

            if str(K) in time_string:
                answer += 1
print(answer)
