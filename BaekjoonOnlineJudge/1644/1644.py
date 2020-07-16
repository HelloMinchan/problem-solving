import sys, bisect
input = sys.stdin.readline

N = int(input())

isPrime = [False] + [False] + [True] * 3999999
primes = []
for i in range(2, 4000001):
    if isPrime[i]:
        primes.append(i)
    for j in range(i * 2, 4000001, i):
        isPrime[j] = False

index = bisect.bisect(primes, N)

answer = 0
for i in range(index):
    sumValue = primes[i]
    if sumValue >= N:
        if sumValue == N:
            answer += 1
        continue
    for j in range(i + 1, index):
        sumValue += primes[j]

        if sumValue >= N:
            if sumValue == N:
                answer += 1
            break

print(answer)
