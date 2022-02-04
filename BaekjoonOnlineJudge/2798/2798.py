import sys

input = sys.stdin.readline


N, M = map(int, (input().split()))
input_cards = sorted(map(int, input().split()), reverse=True)
cards = []

for card in input_cards:
    if card < M:
        cards.append(card)


answer = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            tot = cards[i] + cards[j] + cards[k]

            if tot == M:
                print(tot)
                sys.exit(0)
            elif tot < M:
                answer = max(answer, tot)

print(answer)