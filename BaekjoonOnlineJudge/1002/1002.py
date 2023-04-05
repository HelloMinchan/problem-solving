import sys

input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


T = int(input())

while T:
    T -= 1

    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = get_distance(x1, y1, x2, y2)

    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2):
        print(2)
    else:
        print(0)
