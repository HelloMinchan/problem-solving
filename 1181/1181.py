import sys
input = sys.stdin.readline

words = set([input().rstrip() for _ in range(int(input()))])
print(*sorted(words, key=lambda words: (len(words), words[:])), sep="\n")