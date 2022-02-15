# 11:40 ~ 11:46 (6분)
import sys

input = sys.stdin.readline


def dfs(number):
    if number == 1 or number == 2:
        return 1

    if dp_table[number]:
        return dp_table[number]

    dp_table[number] = dfs(number - 1) + dfs(number - 2)

    return dp_table[number]


n = int(input())

dp_table = [0 for _ in range(n + 1)]

print(dfs(n))
