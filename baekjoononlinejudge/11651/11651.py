import sys
input = sys.stdin.readline

location = [tuple(map(int, input().split())) for _ in range(int(input()))]

for x, y in sorted(location, key=lambda location: (location[1], location[0])):
    print(x, y)