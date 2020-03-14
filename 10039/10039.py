import sys
input = sys.stdin.readline

avg = 0

for score in [int(input()) for _ in range(5)]:
    if score < 40:
        avg += 8
    else:
        avg += score // 5

print(avg)