import sys

input = sys.stdin.readline

X = int(input())

dp_table = [0 for _ in range(X + 1)]

for i in range(2, X + 1):
    minimum_oper = 987654321

    if i % 5 == 0:
        minimum_oper = min(minimum_oper, dp_table[i // 5] + 1)
    if i % 3 == 0:
        minimum_oper = min(minimum_oper, dp_table[i // 3] + 1)
    if i % 2 == 0:
        minimum_oper = min(minimum_oper, dp_table[i // 2] + 1)

    minimum_oper = min(minimum_oper, dp_table[i - 1] + 1)

    dp_table[i] = minimum_oper

print(dp_table[-1])