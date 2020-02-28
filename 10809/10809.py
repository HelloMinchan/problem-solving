import sys
input = sys.stdin.readline

location = [-1] * 26
word = list(input().rstrip())

for index, i in enumerate(word):
    if location[ord(i) - 97] == -1:
        location[ord(i) - 97] = index

for i in location:
    print(i, end=' ')