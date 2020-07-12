import sys, bisect
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
target = list(map(int, input().split()))

for num in target:
    index = bisect.bisect_left(A, num)
    if index < len(A) and A[bisect.bisect_left(A, num)] == num:
        print(1)
    else:
        print(0)
