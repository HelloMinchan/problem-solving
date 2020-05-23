import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for j in range(1, N + 1):
        if j % 2 == 1:
            print("* ", end="")
    print()
    for k in range(1, N + 1):
        if k % 2 == 0:
            print(" *", end="")
    print()