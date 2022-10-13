import sys

input = sys.stdin.readline

chess = [1, 1, 2, 2, 2, 8]
pieces = list(map(int, input().split()))

for kind in range(len(chess)):
    print(chess[kind] - pieces[kind], end=" ")
