import sys
input = sys.stdin.readline

words = sorted(list(set([input().rstrip() for _ in range(int(input()))])), key=lambda x: (len(x), x[:]))
print("\n".join(words))
