from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())

seq = list(map(int, input().split()))

left = 0
right = 1
count_dict = defaultdict(int)
count_dict[seq[left]] = 1
answer = 1

while right < N:
    if count_dict[seq[right]] != 0:
        while count_dict[seq[right]] != 0:
            count_dict[seq[left]] -= 1
            left += 1

    count_dict[seq[right]] += 1
    answer += right - left + 1
    right += 1

print(answer)
