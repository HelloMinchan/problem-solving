from collections import defaultdict
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    W = input().rstrip()
    K = int(input())

    spell_location = defaultdict(list)
    answer = []

    for index, spell in enumerate(W):
        spell_location[spell].append(index)

    for location in spell_location.values():
        if len(location) >= K:
            for i in range(len(location) - K + 1):
                answer.append(location[i + K - 1] - location[i] + 1)

    if answer:
        print(min(answer), max(answer))
    else:
        print(-1)
