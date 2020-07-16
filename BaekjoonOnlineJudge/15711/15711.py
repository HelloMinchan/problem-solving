import sys, bisect
input = sys.stdin.readline

isPrime = [False] + [False] + [True] * (2000000 - 1)

primes = []
for i in range(2, 2000001):
    if isPrime[i]:
        primes.append(i)
        for j in range(i * 2, 2000001, i):
            isPrime[j] = False

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    if A + B < 4:
        print("NO")
    elif not (A + B) % 2:
        print("YES")
    else:
        for n in primes:
            if n >= (A + B - 2):
                print("YES")
                break
            if not (A + B - 2) % n:
                print("NO")
                break
        else:
            print("YES")
