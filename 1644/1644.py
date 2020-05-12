import sys
input = sys.stdin.readline

N = int(input())
isPrime = [False, False] + [True] * (N - 1)
primeSequence = []

for i in range(2, N + 1):
    if isPrime[i]:
        primeSequence.append(i)
        for j in range(2 * i, N + 1, i):
            isPrime[j] = False

startPointer = 0
endPointer = 0
sumValue = 0
ans = 0

while(True):
    if sumValue >= N:
        sumValue -= primeSequence[startPointer]
        startPointer += 1
    elif endPointer == len(primeSequence):
        break
    else:
        sumValue += primeSequence[endPointer]
        endPointer += 1

    if sumValue == N:
        ans += 1

print(ans)