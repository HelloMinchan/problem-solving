import sys

input = sys.stdin.readline


def next_permutation(word):
    i = len(word) - 1
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    if i <= 0:
        return

    j = len(word) - 1
    while word[i - 1] >= word[j]:
        j -= 1
    word[i - 1], word[j] = word[j], word[i - 1]

    j = len(word) - 1
    while i < j:
        word[i], word[j] = word[j], word[i]
        i += 1
        j -= 1


T = int(input())
for _ in range(T):
    word = list(input().rstrip())
    next_permutation(word)
    print("".join(word))
