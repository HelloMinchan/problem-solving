import sys
input = sys.stdin.readline

n = int(input())
n -= 1;

i = n + 1

ans = 0
while i != 0:
    ans += (n // i + 1) * (i - (n // ((n // i) + 1)))
    i = n // ((n // i) + 1)

print(ans)
