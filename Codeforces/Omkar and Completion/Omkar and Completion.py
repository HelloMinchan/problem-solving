import sys
input = sys.stdin.readline

t = int(input())
memoization = [1] * 1000

for _ in range(t):
    n = int(input())
    print(*memoization[:n])
