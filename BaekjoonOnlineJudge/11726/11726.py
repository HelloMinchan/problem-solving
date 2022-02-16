import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(number):
    if number == 1:
        dp_table[number] = 1
        return dp_table[number]
    elif number == 2:
        dp_table[number] = 2
        return dp_table[number]

    if dp_table[number] != -1:
        return dp_table[number]

    dp_table[number] = (dfs(number - 1) + dfs(number - 2)) % 10007

    return dp_table[number]


n = int(input())

dp_table = [-1 for _ in range(n + 1)]

print(dfs(n))