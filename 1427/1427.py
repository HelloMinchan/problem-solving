import sys
input = sys.stdin.readline

num = sorted([int(i) for i in input().rstrip()])
print(*reversed(num), sep="")