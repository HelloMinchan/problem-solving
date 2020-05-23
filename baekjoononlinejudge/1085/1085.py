import sys
input = sys.stdin.readline

x, y, w, h = map(int, input().split())
distance = []
distance.append(w - x)
distance.append(x - 0)
distance.append(h - y)
distance.append(y - 0)

print(min(distance))