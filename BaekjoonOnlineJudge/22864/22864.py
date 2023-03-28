import sys

input = sys.stdin.readline

A, B, C, M = map(int, input().split())

TODAY_HOUR = 24

current_patigue = 0
current_throughput = 0

for _ in range(TODAY_HOUR):
    if current_patigue + A <= M:
        current_patigue += A
        current_throughput += B
    else:
        current_patigue -= C

        if current_patigue < 0:
            current_patigue = 0

print(current_throughput)
