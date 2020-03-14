import sys
input = sys.stdin.readline

N = int(input())
maxLen = N * 2 - 1
empty = 0

for i in range(maxLen, 0, -2):
    for j in range(0, empty):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
    empty += 1

empty -= 2

for i in range(3, maxLen + 1, +2):
    for j in range(0, empty):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
    empty -= 1