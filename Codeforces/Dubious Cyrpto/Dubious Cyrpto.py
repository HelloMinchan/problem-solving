import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, r, m = map(int, input().split())

    temp = m // l

    if temp == 0:
        print(l, r - (m - ((m // l) * l)), r)
    else:
        print(l, r, r - (m - ((m // l) * l)))
