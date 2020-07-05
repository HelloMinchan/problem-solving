import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(n):
        for j in range(m):
            
