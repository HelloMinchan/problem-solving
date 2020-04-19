import sys
input = sys.stdin.readline

num = 1
i = 1

target = int(input())
while True:
    if target > num:
        num += 6 * i
        i += 1
        continue
    break

print(i)