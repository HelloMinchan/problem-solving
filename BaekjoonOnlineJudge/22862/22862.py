import sys

input = sys.stdin.readline

N, K = map(int, input().split())
seq = list(map(int, input().split()))

left = 0
right = 0

while left < N and seq[left] % 2 != 0:
    left += 1

answer = 0
right = left + 1
if left < N:
    answer = 1
odd_count = 0

while right < N:
    if seq[right] % 2 == 0:
        answer = max(answer, right - left + 1 - odd_count)
        right += 1
    else:
        if odd_count < K:
            odd_count += 1
            answer = max(answer, right - left + 1 - odd_count)
            right += 1
        else:
            while seq[left] % 2 == 0:
                left += 1

            odd_count -= 1
            left += 1

print(answer)
