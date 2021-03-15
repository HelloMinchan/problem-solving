import sys

input = sys.stdin.readline

S = int(input())

N = 1
while 1:
    S -= N
    N += 1
    if S - N <= 0:
        break

print(N if S - N == 0 else N - 1)
