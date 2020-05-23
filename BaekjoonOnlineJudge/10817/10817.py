import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
li = []
li.append(a)
li.append(b)
li.append(c)
li.sort()

print(li[1])