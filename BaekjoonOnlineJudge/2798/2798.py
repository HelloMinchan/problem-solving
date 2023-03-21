import sys

input = sys.stdin.readline


def dfs(card_index):
    global answer

    if len(card_stack) == 3:
        card_stack_sum = sum(card_stack)
        if card_stack_sum <= max_sum:
            answer = max(answer, card_stack_sum)
        return

    for next_card_index in range(card_index, card_number):
        if not visit[next_card_index]:
            visit[next_card_index] = True
            card_stack.append(cards[next_card_index])
            dfs(next_card_index + 1)
            visit[next_card_index] = False
            card_stack.pop()


card_number, max_sum = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
card_stack = []
visit = [False for _ in range(card_number)]

dfs(0)

print(answer)
