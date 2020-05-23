import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5

    # 원이 중첩된 경우
    if r1 == r2 and distance == 0:
        print(-1)
    # 원이 외접한 경우
    elif r1 + r2 == distance:
        print(1)
    # 원이 내접한 경우
    elif abs(r1 - r2) == distance:
        print(1)
    # 원끼리 떨어져 있을 경우
    elif r1 + r2 < distance:
        print(0)
    # 원 안에 원이 있지만 교점이 없을 경우
    elif abs(r1 - r2) > distance:
        print(0)
    # 그 외 나머지 경우
    else:
        print(2)