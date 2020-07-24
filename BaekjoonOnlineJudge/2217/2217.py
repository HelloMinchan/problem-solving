import sys
input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)

maxW = 0
for i, rope in enumerate(ropes):
    maxW = max(maxW, rope * (i + 1))

print(maxW)
