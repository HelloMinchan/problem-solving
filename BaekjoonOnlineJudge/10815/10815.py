import sys

input = sys.stdin.readline

N = int(input())
cards1 = set(map(int, input().split()))

M = int(input())
cards2 = list(map(int, input().split()))

for card in cards2:
    if card in cards1:
        print(1, end=" ")
    else:
        print(0, end=" ")