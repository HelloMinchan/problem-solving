import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
hash_card = dict()

for card in cards:
    hash_card[card] = hash_card.get(card, 0) + 1

for num in nums:
    print(hash_card.get(num, 0), end=" ")
