import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
tot = list(str(a * b * c))

for i in range(10):
    print(tot.count(str(i)))