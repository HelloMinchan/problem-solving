import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
hash_card = dict()

for card in cards: hash_card[card] = 1

for num in nums:
    if hash_card.get(num, 0):
        print(1, end=" ")
    else:
        print(0, end=" ")
