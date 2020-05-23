import sys
input = sys.stdin.readline

for _ in range(int(input())):
    count = 0
    a = 1
    x, y = map(int, input().split())

    while True:
        if (a * (a + 1)) // 2 == y - x:
            count += a
            break
        elif (a * (a + 1)) // 2 < y - x:
            x += a
            a += 1
            count += 1
        else:
            a -= 1
            if y - x == 1:
                count += 1
                break
            elif (a * (a + 1)) // 2 == y - x:
                count += a
                break
            elif (a * (a + 1)) // 2 < y - x:
                x += a
                a += 1
                count += 1

    print(count)