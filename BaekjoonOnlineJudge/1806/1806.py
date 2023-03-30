import sys

input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

left = 0
right = 1

total = seq[left]
if total >= S:
    answer = 1
else:
    answer = sys.maxsize

while right < N:
    if total + seq[right] < S:
        total += seq[right]
        right += 1
    else:
        total += seq[right]
        answer = min(answer, right - left + 1)

        while total - seq[left] >= S:
            total -= seq[left]
            left += 1
            answer = min(answer, right - left + 1)

        right += 1

print(answer if answer != sys.maxsize else 0)
