import sys

input = sys.stdin.readline

N, M = map(int, input().split())

print(*sorted(list(map(int, input().split())) + list(map(int, input().split()))))
