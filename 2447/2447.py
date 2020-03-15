import sys
input = sys.stdin.readline


def hanoi(n, start, middle, finish):
    if n == 1:
        print(start, finish)
        return
    hanoi(n - 1, start, finish, middle)
    print(start, finish)
    hanoi(n - 1, middle, start, finish)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)