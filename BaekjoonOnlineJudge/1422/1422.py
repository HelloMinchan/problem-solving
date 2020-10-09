from functools import cmp_to_key
import sys
input = sys.stdin.readline


def compare(x, y):
    if x + y > y + x:
        return 1
    else:
        return -1


K, N = map(int, input().split())
nums = sorted([input().rstrip() for _ in range(K)], key=cmp_to_key(compare), reverse=True)

answer = ""

maxI = 0
maxLength = 0

for i, num in enumerate(nums):
    if maxLength < len(num):
        maxLength = len(num)
        maxI = i

for i, num in enumerate(nums):
    if i == maxI:
        for _ in range(N - K + 1):
            answer += num
    else:
        answer += num

print(answer)
