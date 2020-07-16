import sys
input = sys.stdin.readline

MIN, MAX = map(int, input().split())

num = [True] * (MAX - MIN + 1)

answer = MAX - MIN + 1

i = 1

while i * i <= MAX:
    i += 1
    sq = i * i

    start = MIN // sq

    while sq * start <= MAX:
        index = sq * start - MIN

        if index >= 0 and num[index]:
            answer -= 1
            num[index] = False
        start += 1
    
print(answer)
