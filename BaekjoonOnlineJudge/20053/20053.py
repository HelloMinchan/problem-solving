import sys

input = sys.stdin.readline

T = int(input())

while T:
    T -= 1

    N = int(input())
    nums = list(map(int, input().split()))

    print(min(nums), max(nums))
