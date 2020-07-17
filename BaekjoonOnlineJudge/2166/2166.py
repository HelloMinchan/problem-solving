import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


N = int(input())
x = []
y = []

for _ in range(N):
    tx, ty = map(int, input().split())

    x.append(tx)
    y.append(ty)

area = 0
for i in range(1, N - 1):
    area += ccw(x[0], y[0], x[i], y[i], x[i + 1], y[i + 1])

print("%.1f" % abs(area / 2))
