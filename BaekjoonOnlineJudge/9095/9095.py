# 5:46 ~ 5:55 (9분)
import sys

input = sys.stdin.readline


def dfs(number):
    if number == 1:
        dp_table[number] = 1
        return dp_table[number]
    elif number == 2:
        dp_table[number] = 2
        return dp_table[number]
    elif number == 3:
        dp_table[number] = 4
        return dp_table[number]

    if dp_table[number]:
        return dp_table[number]

    dp_table[number] += dfs(number - 1) + dfs(number - 2) + dfs(number - 3)

    return dp_table[number]


T = int(input())

for _ in range(T):
    n = int(input())

    dp_table = [0 for _ in range(n + 1)]

    print(dfs(n))