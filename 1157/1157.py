import sys
input = sys.stdin.readline

count = []
for i in range(26):
    count.append([0, chr(i + 65)])

word = list(input().rstrip().upper())

for i in word:
    count[ord(i) - 65][0] += 1

count.sort(key=lambda x: x[0], reverse=True)

if count[0][0] == count[1][0]:
    print('?')
else:
    print(count[0][1])