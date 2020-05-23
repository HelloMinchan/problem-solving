import sys
input = sys.stdin.readline

word = list(input().rstrip())
time = 0

for i in word:
    if ord(i) - 64 <= 3:
        time += 3
    elif ord(i) - 64 <= 6:
        time += 4
    elif ord(i) - 64 <= 9:
        time += 5
    elif ord(i) - 64 <= 12:
        time += 6
    elif ord(i) - 64 <= 15:
        time += 7
    elif ord(i) - 64 <= 19:
        time += 8
    elif ord(i) - 64 <= 22:
        time += 9
    elif ord(i) - 64 <= 26:
        time += 10

print(time)