import sys
input = sys.stdin.readline

M, N = map(int, input().split())

isPrime = [False] + [False] + [True] * 999999

for i in range(2, 1000001):
    if isPrime[i]:
        for j in range(i * 2, 1000001, i):
            isPrime[j] = False

for i in range(M, N + 1):
    if isPrime[i]:
        print(i)
