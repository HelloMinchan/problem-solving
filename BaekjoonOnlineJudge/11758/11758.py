import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    # 신발끈 공식
    # temp = x1 * y2 + x2 * y3 + x3 * y1
    # temp = temp - (y1 * x2 + y2 * x3 + y3 * x1)
    temp = ((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)) // 2

    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

print(ccw(x1, y1, x2, y2, x3, y3))
