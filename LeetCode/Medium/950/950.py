from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        order = deque(range(len(deck)))
        new_deck = [0 for _ in range(len(deck))]

        for card in sorted(deck):
            new_deck[order.popleft()] = card

            if order:
                order.append(order.popleft())

        return new_deck
