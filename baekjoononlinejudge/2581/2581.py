import sys
input = sys.stdin.readline


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0: return False
    return True


pn = []

start = int(input())
end = int(input())

for i in range(start, end + 1):
    if isPrime(i):
        pn.append(i)

if len(pn) == 0:
    print(-1)
else:
    print(sum(pn))
    print(min(pn))