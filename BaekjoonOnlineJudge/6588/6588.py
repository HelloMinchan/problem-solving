import sys, bisect
input = sys.stdin.readline

primes = dict()
isPrime = [False] + [False] + [True] * 999999

for i in range(2, 1000001):
    if isPrime[i]:
        primes[i] = 1
        for j in range(i * 2, 1000001, i):
            isPrime[j] = False

primeList = list(primes.keys())

while 1:
    n = int(input())

    if not n:
        break
    
    for i in range(bisect.bisect(primeList, n), -1, -1):
        if primeList[i] % 2:
            if (n - primeList[i]) % 2:
                if primes.get(n - primeList[i], 0):
                    print(n, '=', n - primeList[i], '+', primeList[i])
                    break
    else:
        print("Goldbach's conjecture is wrong.")
