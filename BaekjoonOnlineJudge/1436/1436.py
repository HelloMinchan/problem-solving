import sys

input = sys.stdin.readline

N = int(input())
dp_table = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    dp_table[i] = dp_table[i - 1] + 1

    if i % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)


print(dp_table[-1])
