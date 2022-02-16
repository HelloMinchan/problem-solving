# 2:03 ~
import sys

input = sys.stdin.readline


def dfs(number):
    if number == 1:
        dp_table[number] = 1
    elif number == 2:
        dp_table[number] = 3

    if dp_table[number]:
        return dp_table[number]

    dp_table[number] = dfs(number - 1) + 2 * dfs(number - 2)

    return dp_table[number]


N = int(input())
dp_table = [0 for _ in range(N + 1)]

print(dfs(N))