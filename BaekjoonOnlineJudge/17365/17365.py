import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
target = input().rstrip()

hash_str = dict()

for word in words:
    temp = ""

    for w in word:
        temp += w
        hash_str[temp] = hash_str.get(temp, 0) + 1

print(hash_str)
