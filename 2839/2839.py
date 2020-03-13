import sys
input = sys.stdin.readline

count = 0
n = int(input())

count += n // 5
temp = n % 5

while temp != n:
    if temp % 3 != 0:
        temp += 5
        count -= 1
    else:
        count += temp // 3
        temp = n % 3
        print(count)
        exit()

if temp % 3 == 0:
    count += temp // 3
    print(count)
else:
    print(-1)