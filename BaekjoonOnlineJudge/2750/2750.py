import sys
input = sys.stdin.readline

N = int(input())
arr = map(str, sorted([int(input()) for _ in range(N)]))

print("\n".join(arr))
