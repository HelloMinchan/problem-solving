import sys
input = sys.stdin.readline


def fac(N):
    if N == 0 or N == 1:
        return 1
    return N * fac(N - 1)


print(fac(int(input())))