import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name = dict()
number = dict()

for i in range(1, N + 1):
    poketmon = input().rstrip()

    name[poketmon] = i
    number[i] = poketmon

for _ in range(M):
    order = input().rstrip()

    if order.isdecimal():
        print(number[int(order)])
    else:
        print(name[order])
