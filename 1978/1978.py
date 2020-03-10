import sys
input = sys.stdin.readline


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0: return False
    return True


_ = input()
num = list(map(int, input().split()))
count = 0

for n in num:
    if isPrime(n):
        count += 1

print(count)