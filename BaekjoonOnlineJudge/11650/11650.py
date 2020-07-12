import sys
input = sys.stdin.readline

N = int(input())
coords = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x : (x[0], x[1]))
for coord in coords:
    print(*coord)
