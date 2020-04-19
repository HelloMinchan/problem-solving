import sys
input = sys.stdin.readline

count = 0
N = int(input())

count += N // 5
temp = N % 5

while temp != N:
    if temp % 3 != 0:
        temp += 5
        count -= 1
    else:
        count += temp // 3
        temp = N % 3
        print(count)
        sys.exit(0)

if temp % 3 == 0:
    count += temp // 3
    print(count)
else:
    print(-1)