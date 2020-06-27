import sys
input = sys.stdin.readline

while 1:
    x = input()
    if x == '':
        break
    x = int(x) * (10 ** 7)
    n = int(input())

    lego = [int(input()) for _ in range(n)]
    lego.sort()

    left = 0
    right = len(lego) - 1

    while left < right:
        target = lego[left] + lego[right]

        if target == x:
            print("yes %d %d" % (lego[left], lego[right]))
            break
        else:
            if target > x:
                right -= 1
            else:
                left += 1
    else:
        print("danger")
