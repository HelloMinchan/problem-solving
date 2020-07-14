import sys
input = sys.stdin.readline

N = int(input())
isPrime = [False] + [False] + [True] * 999

for i in range(2, 1001):
    if isPrime[i]:
        for j in range(i * 2, 1001, i):
            isPrime[j] = False

nums = list(map(int, input().split()))
answer = 0

for num in nums:
    if isPrime[num]:
        answer += 1

print(answer)
