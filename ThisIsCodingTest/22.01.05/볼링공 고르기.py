import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bowlings = list(map(int, input().split()))

bucket = [0 for _ in range(11)]
answer = 0

for bowling in bowlings:
    bucket[bowling] += 1

for i in range(1, 10):
    for j in range(i + 1, 11):
        answer += bucket[i] * bucket[j]

print(answer)