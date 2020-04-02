from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

print(round(sum(numbers) / N))
print(numbers[N // 2])

mode = Counter(numbers).most_common()
print(numbers[0] if len(numbers) == 1 or numbers.count(numbers[0]) == N else mode[0][0] if mode[0][1] != mode[1][1] else mode[1][0])
print(0 if len(numbers) == 1 else numbers[-1] - numbers[0])