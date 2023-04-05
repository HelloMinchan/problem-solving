import sys

input = sys.stdin.readline


N = int(input())

MULTI_VALUE = 6
multi_count = 1

now_value = 1

while now_value < N:
    now_value += MULTI_VALUE * multi_count
    multi_count += 1

print(multi_count)
